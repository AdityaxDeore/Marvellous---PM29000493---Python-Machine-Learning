import schedule
import sys
import os
import time
from datetime import datetime


def CreateFile():
    filename = datetime.now().strftime("File_%d_%m_%Y_%H_%M_%S.txt")
    with open(filename, "w") as f:
        f.write("Filename : " + filename + "\n")
        f.write("Creation Date : " + datetime.now().strftime("%d-%m-%Y") + "\n")
        f.write("Creation Time : " + datetime.now().strftime("%I:%M:%S %p"))



def main():
    schedule.every(1).minute.do(CreateFile)
    
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



