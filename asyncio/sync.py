# 동기(Syncronous) 방식
# A작업 -> B작업- 작업이 순차적으로 진행되는 방식 : A작업이 끝나야 B작업이 시작됨

import time


# 함수 정의
# def hello() 피호출자(callee)
def hello():
    time.sleep(3)  # 1초간 대기
    print("Hello")

# 함수 호출
hello()  # 호출자(caller)
