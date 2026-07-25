import sys
import os
import shutil
import datetime

def BackupFile(SourceFile, DestinationDirectory):

    if not os.path.exists(SourceFile):
        print("Marvellous Automation Error: Source file does not exist")
        return

    if not os.path.isfile(SourceFile):
        print("Marvellous Automation Error: It is not a file")
        return

    if not os.path.exists(DestinationDirectory):
        os.mkdir(DestinationDirectory)

    filename = os.path.basename(SourceFile)
    name, extension = os.path.splitext(filename)

    timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    BackupFileName = name + "_" + timestamp + extension

    DestinationFile = os.path.join(DestinationDirectory, BackupFileName)

    shutil.copy(SourceFile, DestinationFile)

    print("Backup completed successfully")
    print("Backup File :", DestinationFile)

    fobj = open("backup_log.txt", "a")

    fobj.write("Marvellous Automation Script\n")
    fobj.write("Backup Operation Details\n")

    logtime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj.write("Backup completed successfully at %s\n" % (logtime))
    fobj.write("\n")

    fobj.close()

    print("Log saved to backup_log.txt")


def main():

    print("File Backup System")

    if(len(sys.argv) == 3):

        Source = sys.argv[1]
        Destination = sys.argv[2]

        BackupFile(Source, Destination)

    else:
        print("Invalid number of arguments")
        print("Usage :")
        print("py Assignement30_7.py <SourceFile> <DestinationFolder>")


if __name__ == "__main__":
    main()