import datetime
import time
import schedule

def time():
    print("Coding kar...",datetime.datetime.now())

def main():
    schedule.every(30).minutes.do(time)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()