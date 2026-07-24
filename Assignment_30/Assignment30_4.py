import datetime
import time
import schedule

def time():
    print("Namaskar.",datetime.datetime.now())

def main():
    schedule.every().day.at("09:00").do(time)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()