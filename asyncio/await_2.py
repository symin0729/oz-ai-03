# 1) await는 반드시 비동기 함수 안에서만 사용 가능하다
import asyncio
import time

# def hello(): ❌
#     await asyncio.sleep(3) # SyntaxError: 'await' outside function
# # await는 반드시 awaitable 객체와 함께 사용해야 한다 
# async def hello():
#     await asyncio.sleep(3)

# 2) await 할 수 있는 코드 앞에만 await를 사용할 수 있다
async def hi():
    # await time.sleep(2) #  time.sleep()함수는 대기 가능하지만, awati는 사용 불가
    await asyncio.sleep(2) # asyncio.sleep()함수는 대기 가능하고, await도 사용 가능 

asyncio.run(hi())



# 3) 
async def hi(): # hi() 비동기 함수, 코루틴 함수 정의
    print("start hello..")
    await asyncio.sleep(2)
    print("end hello..")

async def main():
    print("start main..")
    coro = hi() # hi() 코루틴 객체 생성
    await coro # hi() 코루틴 객체 실행
    print("end main..")

asyncio.run(main())