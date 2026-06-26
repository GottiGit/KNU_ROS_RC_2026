import threading
import time


def task(name, duration):
    print("쓰레드 시작", name)
    time.sleep(duration)
    print("쓰레드 종료", name, duration, "완료")


def main():
    i = 0
    t = threading.Thread(target=task, args=(f"T{i+1}", 5+i))
    t2 = threading.Thread(target=task, args=(f"T{i+1}", 5+i))
    t.start()
    t2.start()
    print("main 실행 중")
    t.join()        # 대기 t 종료 될때 까지
    t2.join()
    print("모든 쓰레드 종료")


if __name__ == "__main__":
    main()
