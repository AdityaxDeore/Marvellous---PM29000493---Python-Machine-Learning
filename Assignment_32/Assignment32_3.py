import os
import sys
import schedule
import time


def DisplayFile(FileName):

    try:
        if not os.path.exists(FileName):
            print("File does not exist")
            return

        if os.path.getsize(FileName) == 0:
            print("File is empty")
            return

        fobj = open(FileName, "r")

        print("\nFile Contents:\n")
        print(fobj.read())

        fobj.close()

    except PermissionError:
        print("Permission is denied")

    except OSError:
        print("File cannot be opened")


def main():

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script displays the contents of a text file every minute.")
            print("Use --u for usage.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("python DisplayFile.py <FilePath>")

        else:
            DisplayFile(sys.argv[1])

            schedule.every(1).minutes.do(DisplayFile, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Use --h or --u for more information")


if __name__ == "__main__":
    main()