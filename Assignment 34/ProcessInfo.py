"""
Question 2:
Write a Python script that defines a user-defined module named ProcessInfo.py.
The module should provide the following functionalities:
- ProcessDetails() - Displays information of the currently running process, including:
    - Process ID (PID)
    - Process name
    - Username
- ProcessCreation() - Creates a new child process using the multiprocessing
  module. The child process should display:
    - Process ID (PID) of the child process
    - Process name of the child process
"""

import multiprocessing
import os
import subprocess

try:
    import psutil
    HasPsutil = True
except ImportError:
    HasPsutil = False


def GetCurrentInfo():
    if HasPsutil:
        p = psutil.Process(os.getpid())
        return p.pid, p.name(), p.username()

    result = subprocess.run(["ps", "-p", str(os.getpid()), "-o", "pid=,comm=,user="],
                            capture_output=True, text=True)
    parts = result.stdout.strip().split()
    return int(parts[0]), parts[1], parts[2]


def ProcessDetails():
    try:
        pid, name, user = GetCurrentInfo()
        print("Process ID (PID) : " + str(pid))
        print("Process Name     : " + name)
        print("Username         : " + user)
    except OSError:
        print("Process details cannot be displayed")


def ChildTask():
    pid, name, user = GetCurrentInfo()
    print("Child Process ID (PID) : " + str(pid))
    print("Child Process Name     : " + name)


def ProcessCreation():
    child = multiprocessing.Process(target=ChildTask)
    child.start()
    child.join()


def main():
    print("--- Current Process Details ---")
    ProcessDetails()
    print("--- Child Process Creation ---")
    ProcessCreation()


if __name__ == "__main__":
    main()
