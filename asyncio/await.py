import time
import asyncio

# 동기 방식으로 작업 실행
# def a():
#     print("A 작업 시작")
#     time.sleep(2)  # 2초간 대기 발생
#     print("A 작업 종료")

# def b():
#     print("B 작업 시작")
#     time.sleep(2)  # 2초간 대기 발생
#     print("B 작업 종료")


# start = time.time()  # 시작 시간 기록   
# a()  # A 작업 실행
# b()  # B 작업 실행 (A 작업이 끝나야 실행됨)
# end = time.time()  # 종료 시간 기록
# print(f"실행시간: {end - start:.2f}초")

# 비동기 방식으로 작업 실행
async def a():
    print("A 작업 시작")        # [1] a() 실행 시작
    await asyncio.sleep(5)    # [2] 5초 대기 -> 양보
    print("A 작업 종료")        # [6] a() 실행 종료


async def b():
    print("B 작업 시작")         # [3] b() 실행 시작
    await asyncio.sleep(2)     # [4] 2초 대기 -> 양보
    print("B 작업 종료")         # [5] b() 실행 종료


async def main():
    coro1 = a()  # A 작업 실행
    coro2 = b()  # B 작업 실행
    await asyncio.gather(coro1, coro2)  # A 작업과 B 작업을 동시에 실행

start = time.time()  # 시작 시간 기록  
asyncio.run(main()) # 프로그램이 동작하는 이유임
end = time.time()  # 종료 시간 기록
print(f"실행시간: {end - start:.2f}초")