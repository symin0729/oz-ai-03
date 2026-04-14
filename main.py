import asyncio

from contextlib import asynccontextmanager
from llama_cpp import Llama
from openai import AsyncOpenAI
from fastapi import FastAPI, Body, Request, Depends
from fastapi.responses import StreamingResponse

from config import settings
from schema import OpenAIResponse



# 추론을 할 때에는 시스템 프롬프트가 필요 #
# 언어 모델에게 규칙을 지정하는 최상위 지시문
SYSTEM_PROMPT = (
    "You are a concise assistant. "
    "Always reply in the same language as the user's input. "
    "Do not change the language. "
    "Do not mix languages."
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.llm = Llama(
        model_path="./models/Llama-3.2-1B-Instruct-Q4_K_M.gguf",
        n_ctx=4096,
        n_threads=2,
        verbose=False,
        chat_format="llama-3",
    )
    app.state.openai_client = AsyncOpenAI(api_key=settings.openai_api_key)
    yield


app = FastAPI(lifespan=lifespan)


def get_llm(request: Request):
    return request.app.state.llm

def get_openai_client(request: Request):
    return request.app.state.openai_client



# 요청객체(-request)에서 llm 객체를 접근할 수 있게 도와주는 의존성 함수
@app.post("/chats")
async def generate_chat_handler(
    user_input: str = Body(..., embed=True), # {"user_input": "Python이란 뭐야?"}
    llm: Llama = Depends(get_llm)
):
    
    async def event_generator():
        # CPU-bound작업이라 대기 발생 X
        result = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            max_tokens=256,
            temperature=0.7,
            # 응답을 토큰 단위로 스트리밍해서 받아올 수 있게 해주는 옵션
            stream=True
        )
        # result는 제너레이터 객체이므로, 토큰 단위로 응답이 도착할 때마다 출력할 수 있습니다.
        for chunk in result:
            token = chunk["choices"][0]["delta"].get("content")
            if token:
                yield token
                await asyncio.sleep(0.2) # CPU-bound 작업이라 강제로 제어권 반납


    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )


@app.post("/openai")
async def openai_handler(
    user_input: str = Body(..., embed=True),
    openai_client = Depends(get_openai_client),
):
    
    async def event_generator():
        async with openai_client.responses.stream(
            model="gpt-4.1-mini",
            input=user_input,
            text_format=OpenAIResponse,
        ) as stream:
            async for event in stream:
                # 텍스트 토큰
                if event.type == "response.output_text.delta":
                    yield event.data
                
                # 연결 종료
                elif event.type == "response.completed":
                    break

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

    # if response.confidence <= 0.95:
    #     return {"msg": "자신이 없습니다."}

    # if response.output_parsed.confidence <= 0.5:
    #     return # 재시도
    # return response.output_parsed


    # 음식사진 분석 -> 탄/단/지 {"fat" : 10.1, "protein": 20.5, "carbo": 50.2"}
    # AI가 분석한 결과를 : 이 음식은 영양소가 고르게 구성되어 있는 좋은 음식입니다.
    # 우리는 구체적인 응답을 원할 때({"fat" : 10.1, "protein": 20.5, "carbo": 50.2"}) -> 이런 형식으로 지정할 수 있음
    # 1) 방법 : 시스템 프롬프트에서 응답 형식 지정하기
    # 2) pydantic 모델 만들어서 응답 형식 지정하기 -> FastAPI에서 지원하는 기능 -> AI가 응답을 생성할 때, 우리가 미리 정의한 pydantic 모델의 형식에 맞춰서 응답을 생성하도록 유도할 수 있음


    # (이력서) -> 이력서 첨삭 요청 -> 응답형식 : 이력서 (파일) / (사진)
    



