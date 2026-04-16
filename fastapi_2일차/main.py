from fastapi import FastAPI, Path, Query
from request import UserCreateRequest
from response import UserResponse


app = FastAPI()

# @ : Python 데코레이터 : 파이썬 함수에 추가적인 기능을 부여하는 문법

# Get /(root) 요청이 들어오면, root_hanlder라는 함수를 실행해라
@app.get("/")
def root_hanlder():
    return {"ping": "pomg"}

@app.get("/hello")
def hello_hanlder():
    return {"message": "Hello from FastAPI!"}

# 임시 데이터베이스
users = [
    {"id": 1, "name": "alex", "job": "student"},
    {"id": 2, "name": "bob", "job": "sw engineer"},
    {"id": 3, "name": "chris", "job": "barista"},
]


# 전체 사용자 목록 조회 API
# REST API 형식 
# Get / users
@app.get("/users")
def get_users_hanlder():
    return users

# 사용자 정보 검색 API
# GET /users/search?name=alex -> name이 alex인 사용자 검색
# GET /users/search?job=student -> job이 student인 사용자 검색
@app.get("/users/search")
def search_user_handler(
    name: str | None = Query(None),
    job: str | None = Query(None),
    ):
    
    if name is None and job is None:   # 값이 아무것도 없다
        return {"msg": "조회에 사용할 QueryParam이 필요합니다."}
    

    for user in users:
        if name and job and user["name"] == name and user["job"] == job:
            return user
        else:
            if user["name"] == name:
                return user
            if user["job"] == job:
                return user




# 단일 사용자 데이터 조회 API
# GET / users/{user_id} -> {user_id}번 사용자 데이터 조회
# GET / users/1 -> 1번 사용자 데이터 조회

@app.get("/users/{user_id}")
def get_user_one_handler(
    # user_id는 interger 타입으로, Path경로에서 오는 (...)는 필수값이라는 의미
    # Path(..., ge 특정 조건을 검사하는 로직 넣을 수 있음)
    # 이상 (= Greater than or Eual to) 조건을 검사하는 로직 넣을 수 있음
    # user_id에 Path(..., ge=1) 기본값 할당함 : 값이 1 이상인지 기본적으로 확인해줌
    # 선언형 프로그래밍
    user_id: int = Path(..., ge=1),
):
      
    for user in users:
        if user["id"] == user_id:
            return user
    # return None
        # return None 숨어 있음 -> 데이터가 없다면 fastapi문서에서 null로 반환됨

# 회원 추가 API
# POST /users -> 사용자 데이터 추가
@app.post("/users", response_model=UserResponse)
def create_user_handler(
    # 1) 사용자 데이터를 넘겨 받는다 + 데이터 유효성 검사
    body: UserCreateRequest
):
    # 2) 사용자 데이터를 저장한다
    new_user = {
        "id": len(users) + 1,  # 나중에는 db에 의해 id는 자동생성
        "name": body.name,
        "job": body.job,
    }
    users.append(new_user)
    
    
    # 3) 응답을 반환하다
    return new_user


