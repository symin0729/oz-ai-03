import asyncio
import time

# async def good_job():
#     print("[G] 양보합니다...")
#     await asyncio.sleep(2)
#     print("[G] 돌려 받았습니다...")

# # 동기식으로 진행
# async def bad_job():
#     print("[B] 양보 안합니다...")
#     time.sleep(5)
#     print("[B] 계속 진행...")

# async def main():
#     coro1 = good_job()
#     coro2 = bad_job()
#     await asyncio.gather(coro1, coro2)

# asyncio.run(main())

# 정상적인 경우 : 문법도 비동기 방식으로 작성되어야 하고, 함수도 비동기 함수로 작성되어야 함
async def request1():
    print("[1] 새로운 웹 요청...")
    await asyncio.sleep(2)
    print("[1] 응답...")

async def request2():
    print("[2] 새로운 웹 요청...")
    await asyncio.sleep(5)
    print("[2] 응답...")

async def main():
    coro1 = request1()
    coro2 = request2()
    await asyncio.gather(coro1, coro2)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"{end - start:.2f}")


# 비정상적인 경우
async def request1():
    print("[1] 새로운 웹 요청...")
    await asyncio.sleep(2)
    print("[1] 응답...")

async def request2():
    print("[2] 새로운 웹 요청...")
    time.sleep(5)
    print("[2] 응답...")

async def main():
    coro1 = request1()
    coro2 = request2()
    await asyncio.gather(coro1, coro2)

async def main():
    coro1 = request1()
    coro2 = request2()
    await asyncio.gather(coro1, coro2)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"{end - start:.2f}")


