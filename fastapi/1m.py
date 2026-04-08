from fastapi import FastAPI
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

# serch API
@app.get("/users/sarch")
def serach_user_handler():
    return {"msg": "searching..."}



# 단일 사용자 데이터 조회 API
# GET / users/{user_id} -> {user_id}번 사용자 데이터 조회
@app.get("/users/{user_id}")
def get_user_one_handler(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
        # return None 숨어 있음 -> 데이터가 없다면 fastapi문서에서 null로 반환됨



