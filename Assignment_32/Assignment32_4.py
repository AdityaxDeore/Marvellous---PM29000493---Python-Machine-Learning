import os
import sys
import shutil
import schedule
import time
from datetime import datetime


def CopyFiles(Source, Destination):

    if not os.path.exists(Source):
        print("Source directory does not exist")
        return

    if not os.path.exists(Destination):
        print("Destination directory does not exist")
        return

    LogFile = open("CopyLog.txt", "a")

    for FolderName, SubFolder, FileName in os.walk(Source):
        for File in FileName:

            if File.endswith(".txt"):

                SourceFile = os.path.join(FolderName, File)
                DestinationFile = os.path.join(Destination, File)

                try:
                    shutil.copy(SourceFile, DestinationFile)

                    LogFile.write(File + " Copied at " +
                                  datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

                except Exception:
                    print(File, "cannot be copied")

    LogFile.close()


def main():

    if len(sys.argv) == 3:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script copies all .txt files every 10 minutes.")
            print("Use --u for usage.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("python Assignment32_4.py <SourceDir> <DestinationDir>")

        else:
            CopyFiles(sys.argv[1], sys.argv[2])

            schedule.every(10).minutes.do(CopyFiles, sys.argv[1], sys.argv[2])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")


if __name__ == "__main__":
    main()
