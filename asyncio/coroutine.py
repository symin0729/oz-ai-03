# 동기식
# 1) 함수의 정의 : def foo():
# 2) 함수의 호출(불러오기) : foo() => 함수 실행
#                             호출을 하면(불러오기에 대한 결과로) 함수가 실행됨

# 비동기식
# 1) 코루틴 함수(coroutine function) 정의 : async def boo():
# 2) 코루틴 호출 : coro = boo() => 코루틴 객체 생성
# 3) 코루틴 실행 : await boo() 또는 asyncio.run(boo())

import asyncio

async def hello():
    print("hello")

# 동기화 함수에서는 None이 출력되지만, 비동기화 함수에서는 코루틴 객체가 출력됨

coro1 = hello() # 코루틴 객체 생성
coro2 = hello()


# 코루틴 객체 실행 : 그냥 실행시킬 수 없고, await, asyncio.run() 함수 사용
# asyncio.run(coro1)

# 2개 이상의 코루틴을 호출해야 하는 상황
# asyncio.run(coro1, coro2) # 불가능함

async def main():
    await asyncio.gather(coro1, coro2) # 여러 코루틴을 동시에 실행할 수 있도록 도와주는 함수

main_coro = main() # main() 코루틴 객체 생성
asyncio.run(main_coro) # main() 코루틴 실행
