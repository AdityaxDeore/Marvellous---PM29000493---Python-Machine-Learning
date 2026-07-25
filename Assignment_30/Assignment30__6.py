import datetime
import schedule
import time

def lunch():
    print("Lunch Time !",datetime.datetime.now())

def Work():
    print("Wrap up Work !",datetime.datetime.now())


def main():
    schedule.every().day.at("13:00").do(lunch)
    schedule.every().day.at("18:00").do(Work)



    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()