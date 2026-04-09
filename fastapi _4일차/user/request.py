# 요청 본문의 데이터 형식을 관리

from pydantic import BaseModel, Field

# 사용자 추가할 때, 클라이언트가 서버로 보내느 데이터의 형식
# id 는 자동생성하게끔 하려고 적지 않음
class UserCreateRequest(BaseModel):
    name: str  = Field(..., min_length=2, max_length=10)
    job: str

# 사용자 데이터를 수정할 때 데이터 형식
class UserUpdateRequest(BaseModel):
    job: str
    

