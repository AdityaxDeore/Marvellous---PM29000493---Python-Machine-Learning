import os
import sys
import schedule
import time
from datetime import datetime


def FileMonitor(FileName):

    if not os.path.exists(FileName):
        print("File does not exist")
        return

    size = os.path.getsize(FileName)

    fobj = open("FileSizeLog.txt", "a")

    fobj.write("File Path : " + FileName + "\n")
    fobj.write("File Size : " + str(size) + " Bytes\n")
    fobj.write("Date & Time : " +
               datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n\n")

    fobj.close()

    print("Information added to FileSizeLog.txt")


def main():

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script monitors the size of a file every 30 seconds.")
            print("Use --u for usage.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("python FileMonitor.py <FilePath>")

        else:
            FileMonitor(sys.argv[1])

            schedule.every(30).seconds.do(FileMonitor, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Use --h or --u for more information")


if __name__ == "__main__":
    main()