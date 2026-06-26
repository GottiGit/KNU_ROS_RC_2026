import asyncio


async def task(name, duration):
    print("쓰레드 시작", name)
    await asyncio.sleep(duration)
    print("쓰레드 종료", name, duration, "완료")


async def main():
    t1 = asyncio.create_task(task("t1", 5))
    t2 = asyncio.create_task(task("t2", 5))
    print("main 실행 중")
    await t1
    await t2
    print("모든 쓰레드 종료")


if __name__ == "__main__":
    asyncio.run(main())
