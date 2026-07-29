"""
Question 3:
Write an automation script named PeriodicProcessLogger.py that accepts a time
interval in seconds as a command line argument. The script should periodically
log information about the currently running process to a file named
ProcessLog.txt after every specified time interval. The log information should
include:
- Log timestamp
- Process ID (PID)
- Process name
- Username

Example: python PeriodicProcessLogger.py 60
"""

import sys
import time
from datetime import datetime

from ProcessInfo import GetCurrentInfo

LogFileName = "ProcessLog.txt"


def WriteLog():
    try:
        pid, name, user = GetCurrentInfo()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file = open(LogFileName, "a")
        log_file.write("Timestamp: " + timestamp + " | PID: " + str(pid) +
                       " | Process Name: " + name + " | Username: " + user + "\n")
        log_file.close()
    except OSError:
        print("Log file cannot be written")


def StartLogging(Interval, Iterations):
    if Interval <= 0:
        print("Error: interval must be greater than 0")
        return

    count = 0
    try:
        while True:
            time.sleep(Interval)
            WriteLog()
            count = count + 1
            if Iterations > 0 and count >= Iterations:
                break
    except KeyboardInterrupt:
        print("Logger stopped")


def main():
    print("AutomationScript Started")

    if len(sys.argv) == 2 or len(sys.argv) == 3:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script periodically logs the current process info to ProcessLog.txt.")
            print("Use --u for usage.")
            return
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("python PeriodicProcessLogger.py <IntervalInSeconds> [Iterations]")
            return

        interval = int(sys.argv[1])
        iterations = 0
        if len(sys.argv) == 3:
            iterations = int(sys.argv[2])
        StartLogging(interval, iterations)
    else:
        print("Invalid number of arguments")
        print("Use --h or --u for more information")


if __name__ == "__main__":
    main()
