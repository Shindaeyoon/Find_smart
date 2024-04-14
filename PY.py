#HELLO WORLD XD
#async/await

#Coroutine

#예제
# import asyncio as asy

# async def main():
#     print("hello")
#     await asy.sleep(1)
#     print("world")

# asy.run(main())
# '''
# 실행 시 hello출력 후 1초 뒤 world 출력
# '''


# import asyncio as asy
# import time as t

# async def say_after(delay, what):
#     await asy.sleep(delay)
#     print(what)

# async def main():
#     print(f"started at {t.strftime('%X')}")

#     await say_after(1,"hello")
#     await say_after(2,"world")

#     print(f"finished at {t.strftime('%X')}")

# asy.run(main())
# '''
# 실행 시 started출력이 되고 1초 후 hello 그 후 2초후 would 출력
# '''


# import asyncio as asy
# import time as t

# async def say_after(delay, what):
#     await asy.sleep(delay)
#     print(what)

# async def main():
#     task1 = asy.create_task(
#         say_after(1, "hello"))
#     task2 = asy.create_task(
#         say_after(2, "would"))

#     print(f"started at {t.strftime('%X')}")

#     await task1
#     await task2

#     print(f"finished at {t.strftime('%X')}")