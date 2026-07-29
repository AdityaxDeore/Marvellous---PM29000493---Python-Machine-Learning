"""
Question 1:
Write an automation script named ProcessMonitor.py which accepts a process
name as a command line argument and displays the information of all running
processes which have the given name in their name. The script should display
the following information for each process:
- Process ID (PID)
- Process name
- Username

Example: python ProcessMonitor.py python
"""

import os
import subprocess
import sys

try:
    import psutil
    HasPsutil = True
except ImportError:
    HasPsutil = False


def GetProcessList():
    if HasPsutil:
        processes = []
        for p in psutil.process_iter(["pid", "name", "username"]):
            processes.append((p.info["pid"], p.info["name"], p.info["username"]))
        return processes

    result = subprocess.run(["ps", "-eo", "pid,comm,user"], capture_output=True, text=True)
    processes = []
    for line in result.stdout.splitlines()[1:]:
        parts = line.split()
        if len(parts) >= 3:
            processes.append((int(parts[0]), parts[1], parts[2]))
    return processes


def FindProcesses(ProcessName):
    matches = []
    for pid, name, user in GetProcessList():
        if name is None:
            continue
        if ProcessName.lower() in name.lower():
            matches.append((pid, name, user))
    return matches


def DisplayProcesses(ProcessList, ProcessName):
    if not ProcessList:
        print("No running process found matching '" + ProcessName + "'.")
        return

    for pid, name, user in ProcessList:
        print("Process ID (PID) : " + str(pid))
        print("Process Name     : " + name)
        print("Username         : " + user)
        print("-" * 30)


def main():
    print("AutomationScript Started")

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script displays information of all running processes matching a name.")
            print("Use --u for usage.")
            return
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("python ProcessMonitor.py <ProcessName>")
            return
        process_name = sys.argv[1]
        matches = FindProcesses(process_name)
        DisplayProcesses(matches, process_name)
    else:
        print("Invalid number of arguments")
        print("Use --h or --u for more information")


if __name__ == "__main__":
    main()
