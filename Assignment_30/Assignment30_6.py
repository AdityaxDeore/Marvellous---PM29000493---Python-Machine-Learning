import schedule
import os
import sys
import time
import datetime

def logfile():
    fobj = open("Marvellous.txt","a")

    CurrentTime = datetime.datetime.now()

    fobj.write("Task executed at: ")
    fobj.write(str(CurrentTime))
    fobj.write("\n")

    fobj.close()


def main():
    schedule.every(2).minutes.do(logfile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()