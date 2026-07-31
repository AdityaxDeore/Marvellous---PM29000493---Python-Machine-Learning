
import schedule
import time
import os
import sys
from datetime import datetime

def DirectoryScanner(DirectoryPath):
    if not os.path.exists(DirectoryPath):
        print(f"Error: Directory '{DirectoryPath}' does not exist.")
        return

    TotalFiles = 0 
    TotalDirectories = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        TotalFiles += len(FileName)
        TotalDirectories += len(SubFolder)

    print("\nDirectory Scanned :", DirectoryPath)
    print("Total Files       :", TotalFiles)
    print("Total Directories :", TotalDirectories)
    print("Scan Time         :", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script scans a specified directory every minute.")
            print("Use --u for usage.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("python script.py <Path>")
            print("Path should be an Absolute Path.")

        else:
            DirectoryScanner(sys.argv[1])

            schedule.every(1).minutes.do(DirectoryScanner, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Error: Invalid number of arguments.")
        print("Use --h for help and --u for usage.")




if __name__ ==  "__main__":
    main()