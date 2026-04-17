import uuid
import json

from fastapi import FastAPI, Body
from fastapi.responses import StreamingResponse
from redis import asyncio as aredis


# 2) Redis 클라이언트 설정
redis_client = aredis.from_url("redis://redis:6379", decode_responses=True) 
# ("redis://<ip><port>")  
# redis는 bytes로 데이터를 주고받기 때문에 decode_responses=True 옵션을 사용하여 문자열로 자동 디코딩하도록 설정

app = FastAPI()

@app.post("/chats")
async def generate_chat_handler(
    # 1) 요청 본문 정의 : user_input
    user_input: str = Body(..., embed=True)
):
     
    # 2) 채널 구독 - SUBSCRIBE 채널 구독 먼저 해놓음(대기 중...) : Redis의 Pub/Sub 기능 활용
    channel = str(uuid.uuid4())  # 구독할 채널 이름 / uuid로 고유한 채널 이름 생성
    # pubsub 객체 생성 후 subscribe 메서드로 채널 구독
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel)


    # 3) 처리 : Queue를 통해 Worker에 Task를 전달(enqueue)
    task = {"channel": channel, "user_input": user_input}  # 작업(task) 객체 생성 - 채널 이름과 사용자 입력을 포함하는 python의 딕셔너리 형태로 작업 객체 생성 - python의 자료구조
    # redis_client.lpush("queue", task)  # "queue"라는 이름의 Redis 리스트에 task를 추가하는 명령어 - Redis의 자료구조
    # redis는 JSON 기반의 자료구조로 변환해야 함 - 문자열로 데이터를 저장하기 때문에 task 객체를 문자열로 변환하여 저장해야 함 - json.dumps(task)로 변환하여 저장
    await redis_client.lpush("queue", json.dumps(task))  


    # 4) 채널 메시지 읽고 토큰 반환
    async def event_generator():
        async for message in pubsub.listen():
            if message["type"] != "message":
                continue  # 메시지 타입이 "message"가 아닌 경우 무시

            token = message["data"]  # 메시지 데이터 추출
            if token == "[DONE]":
                break  # 토큰이 "[DONE]"인 경우 루프 종료 - 임의로 약속을 함
            yield token 

        await pubsub.unsubscribe(channel)  # 채널 구독 해제 - 루프가 종료된 후에 채널 구독 해제
        await pubsub.close()  # pubsub 객체 닫기 - 리소스 정리


    # 5) 결과 수신
    # StreamingResponse 객체를 반환하여 서버에서 클라이언트로 실시간으로 데이터를 스트리밍할 수 있도록 설정
    #  - event_generator 함수는 pubsub 객체를 인자로 받아서 Redis에서 메시지를 읽어오는 제너레이터 함수
    #  - media_type="text/event-stream"은 서버에서 클라이언트로 전송되는 데이터의 형식을 지정하는 부분
    #  - Server-Sent Events(SSE) 형식으로 데이터를 전송하기 위해 "text/event-stream"으로 설정

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
    )



