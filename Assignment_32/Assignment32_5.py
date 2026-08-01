import os
import sys
import schedule
import time


def DeleteEmptyFiles(Directory):

    if not os.path.exists(Directory):
        print("Directory does not exist")
        return

    LogFile = open("DeleteLog.txt", "a")

    for FolderName, SubFolder, FileName in os.walk(Directory):
        for File in FileName:

            FilePath = os.path.join(FolderName, File)

            try:
                if os.path.getsize(FilePath) == 0:
                    os.remove(FilePath)

                    LogFile.write(FilePath + "\n")
                    print(FilePath, "Deleted")

            except PermissionError:
                print("Permission denied:", FilePath)

    LogFile.close()


def main():

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script deletes all empty files every hour.")
            print("Use --u for usage.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("python Assignment32_5.py <Directory>")

        else:
            DeleteEmptyFiles(sys.argv[1])

            schedule.every(1).hours.do(DeleteEmptyFiles, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")


if __name__ == "__main__":
    main()
