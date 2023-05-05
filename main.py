import os
import time


def shutdown():
    with open("settings.txt", 'r') as f:
        a = f.readline()
        onPC = int(a.split(',')[0])
        offPC = int(a.split(',')[1])
    while offPC > time.localtime().tm_hour >= onPC:
        print("Wait...")
        time.sleep(60)  # ожидание 1 минуту
    os.system('shutdown -s -t 0')
    # os.system('shutdown /p /f')


if __name__ == "__main__":
    shutdown()
