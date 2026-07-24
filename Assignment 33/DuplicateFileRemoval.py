"""
Duplicate File Removal Automation Using Python.

Objective:
Design and develop a Python automation script that periodically scans a
specified directory, identifies duplicate files using file checksums,
deletes the duplicate files, generates a detailed log file, and sends
the log file through email.

Command-Line Execution:
python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>

Example:
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
"""

import os
import sys
import time
from datetime import datetime

import duplicate_utils

SenderEmail = os.environ.get("SENDER_EMAIL", "your_email@gmail.com")
SenderPassword = os.environ.get("SENDER_APP_PASSWORD", "your_app_password")


def PerformCleanup(DirectoryPath, ReceiverEmail, LogPath):
    errors = []

    start_time = datetime.now()
    start_text = start_time.strftime("%d %B %Y, %I:%M:%S %p")

    files = duplicate_utils.ScanDirectory(DirectoryPath, errors)
    duplicate_groups = duplicate_utils.FindDuplicates(files, errors)
    deleted_files = duplicate_utils.DeleteDuplicates(duplicate_groups, errors)

    files_scanned = len(files)
    duplicates_found = sum(len(paths) - 1 for paths in duplicate_groups.values())
    duplicates_deleted = len(deleted_files)

    end_text = datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

    duplicate_utils.WriteLog(LogPath, "Starting time of directory scanning: " + start_text)
    duplicate_utils.WriteLog(LogPath, "Completion time of directory scanning: " + end_text)
    duplicate_utils.WriteLog(LogPath, "Name of the directory scanned: " + DirectoryPath)
    duplicate_utils.WriteLog(LogPath, "Total number of files scanned: " + str(files_scanned))
    duplicate_utils.WriteLog(LogPath, "Total number of duplicate files found: " + str(duplicates_found))
    duplicate_utils.WriteLog(LogPath, "Total number of duplicate files deleted: " + str(duplicates_deleted))

    duplicate_utils.WriteLog(LogPath, "Checksum values of duplicate files:")
    for checksum in duplicate_groups:
        duplicate_utils.WriteLog(LogPath, "  " + checksum)

    duplicate_utils.WriteLog(LogPath, "Complete paths of deleted duplicate files:")
    for path in deleted_files:
        duplicate_utils.WriteLog(LogPath, "  " + path)

    if errors:
        duplicate_utils.WriteLog(LogPath, "Errors encountered during execution:")
        for error in errors:
            duplicate_utils.WriteLog(LogPath, "  " + error)

    body = duplicate_utils.BuildEmailBody(start_text, end_text, DirectoryPath,
                                          files_scanned, duplicates_found, duplicates_deleted)
    email_status = duplicate_utils.SendEmail(SenderEmail, SenderPassword, ReceiverEmail,
                                             "Duplicate File Removal Log", body, LogPath)
    duplicate_utils.WriteLog(LogPath, "Email delivery status: " + email_status)


def main():
    print("Jay Ganesh")

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H" or sys.argv[1] == "--help":
            duplicate_utils.DisplayHelp()
            return
        if sys.argv[1] == "--u" or sys.argv[1] == "--U" or sys.argv[1] == "--usage":
            duplicate_utils.DisplayUsage()
            return

    if len(sys.argv) != 4:
        print("Invalid number of arguments")
        print("Use --h or --u for more information")
        return

    dir_path = sys.argv[1]
    interval_text = sys.argv[2]
    receiver_email = sys.argv[3]

    error = duplicate_utils.ValidateDirectory(dir_path)
    if error:
        print("Error: " + error)
        return

    interval_minutes, error = duplicate_utils.ValidateInterval(interval_text)
    if error:
        print("Error: " + error)
        return

    error = duplicate_utils.ValidateEmail(receiver_email)
    if error:
        print("Error: " + error)
        return

    try:
        log_directory = duplicate_utils.CreateLogDirectory()
    except OSError:
        print("Error: cannot create log directory")
        return

    try:
        while True:
            log_path = duplicate_utils.CreateLogFile(log_directory)
            PerformCleanup(dir_path, receiver_email, log_path)
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("Automation stopped")


if __name__ == "__main__":
    main()
