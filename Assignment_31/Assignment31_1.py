import os 
import sys 
import time
import datetime
import schedule

def message():
    pass


def main():
    x = int(input("Enter Message: "))
    message(x)

    schedule.every(5).seconds.do(message)

if __name__ == "__main__":
    main()