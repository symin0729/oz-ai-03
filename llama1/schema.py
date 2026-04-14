from pydantic import BaseModel, Field

# OpenAI API로부터 받은 응답의 형식을 정의하는 pydantic 모델
class OpenAIResponse(BaseModel):
    result: str = Field(description="최종 답변")
    confidence: float = Field(description="0~1 사이의 신뢰도")

# 강제로 하는 이유
# 1) 일관된 답변 얻기 위해
# 2) 