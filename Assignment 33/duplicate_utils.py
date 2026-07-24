"""
User-defined module for Duplicate File Removal Automation.

Stores all user-defined functions used by DuplicateFileRemoval.py:
directory validation, checksum calculation, duplicate detection and
deletion, log directory and log file handling, and email notification.
"""

import hashlib
import os
import re
import smtplib
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

LogDirectoryName = "Marvellous"


def DisplayHelp():
    print("Duplicate File Removal Automation")
    print("=================================")
    print("Description:")
    print("  Periodically scans a directory, detects duplicate files using")
    print("  MD5 checksums, deletes duplicate copies, generates a timestamped")
    print("  log file and emails the log to the receiver.")
    print()
    print("Use --u for usage.")


def DisplayUsage():
    print("python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>")


def ValidateDirectory(DirectoryPath):
    if not DirectoryPath:
        return "Directory path is not provided."
    if not os.path.isabs(DirectoryPath):
        return "Directory path must be an absolute path."
    if not os.path.exists(DirectoryPath):
        return "Directory does not exist: " + DirectoryPath
    if not os.path.isdir(DirectoryPath):
        return "Path is not a directory: " + DirectoryPath
    if not os.access(DirectoryPath, os.R_OK):
        return "No permission to access directory: " + DirectoryPath
    return None


def ValidateInterval(IntervalText):
    if not IntervalText:
        return None, "Time interval is not provided."

    if not IntervalText.isdigit():
        return None, "Time interval must be a valid numeric value."

    minutes = int(IntervalText)
    if minutes <= 0:
        return None, "Time interval must be greater than zero."

    return minutes, None


def ValidateEmail(EmailAddress):
    if not EmailAddress:
        return "Email address is not provided."

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if not re.match(pattern, EmailAddress):
        return "Invalid email address format: " + EmailAddress

    return None


def CreateLogDirectory():
    directory = os.path.join(os.getcwd(), LogDirectoryName)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def CreateLogFile(LogDirectory):
    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    filename = "DuplicateRemovalLog_" + timestamp + ".log"
    return os.path.join(LogDirectory, filename)


def WriteLog(LogPath, Message):
    try:
        log_file = open(LogPath, "a", encoding="utf-8")
        log_file.write(Message + "\n")
        log_file.close()
    except OSError:
        print("Log file cannot be written")


def CalculateChecksum(FilePath, Errors):
    if not os.path.isfile(FilePath):
        Errors.append("Not a regular file: " + FilePath)
        return None
    if not os.access(FilePath, os.R_OK):
        Errors.append("File is not readable: " + FilePath)
        return None

    try:
        digest = hashlib.md5()
        handle = open(FilePath, "rb")
        while True:
            chunk = handle.read(8192)
            if not chunk:
                break
            digest.update(chunk)
        handle.close()
        return digest.hexdigest()
    except OSError:
        Errors.append("Checksum failed for: " + FilePath)
        return None


def ScanDirectory(DirectoryPath, Errors):
    file_list = []
    for root, dirs, files in os.walk(DirectoryPath):
        for name in files:
            path = os.path.join(root, name)
            if os.path.isfile(path):
                file_list.append(path)
    return file_list


def FindDuplicates(FileList, Errors):
    groups = {}
    for path in FileList:
        checksum = CalculateChecksum(path, Errors)
        if checksum is None:
            continue
        if checksum not in groups:
            groups[checksum] = []
        groups[checksum].append(path)

    duplicates = {}
    for checksum in groups:
        if len(groups[checksum]) > 1:
            duplicates[checksum] = groups[checksum]
    return duplicates


def DeleteDuplicates(DuplicateGroups, Errors):
    deleted = []
    for paths in DuplicateGroups.values():
        for path in paths[1:]:
            try:
                if not os.access(path, os.W_OK):
                    Errors.append("File cannot be deleted: " + path)
                    continue
                os.remove(path)
                deleted.append(path)
            except OSError:
                Errors.append("Delete failed for: " + path)
    return deleted


def BuildEmailBody(StartTime, EndTime, Directory, Scanned, Found, Deleted):
    body = "Jay Ganesh,\n\n"
    body += "The duplicate-file removal operation has been completed successfully.\n\n"
    body += "Starting time of scanning: " + StartTime + "\n"
    body += "Completion time of scanning: " + EndTime + "\n"
    body += "Name of scanned directory: " + Directory + "\n"
    body += "Total number of files scanned: " + str(Scanned) + "\n"
    body += "Total number of duplicate files found: " + str(Found) + "\n"
    body += "Total number of duplicate files deleted: " + str(Deleted) + "\n\n"
    body += "Please find the detailed log file attached to this email.\n\n"
    body += "Regards,\n"
    body += "Marvellous Automation System"
    return body


def SendEmail(SenderEmail, SenderPassword, ReceiverEmail, Subject, Body, AttachmentPath):
    message = MIMEMultipart()
    message["From"] = SenderEmail
    message["To"] = ReceiverEmail
    message["Subject"] = Subject
    message.attach(MIMEText(Body, "plain"))

    try:
        handle = open(AttachmentPath, "rb")
        part = MIMEApplication(handle.read(), Name=os.path.basename(AttachmentPath))
        handle.close()
        part["Content-Disposition"] = 'attachment; filename="' + os.path.basename(AttachmentPath) + '"'
        message.attach(part)
    except OSError:
        return "Email not sent - log file cannot be opened"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=20)
        server.starttls()
        server.login(SenderEmail, SenderPassword)
        server.send_message(message)
        server.quit()
        return "Email sent successfully to " + ReceiverEmail
    except smtplib.SMTPAuthenticationError:
        return "Email not sent - authentication failed. Check sender email and app password."
    except (smtplib.SMTPException, OSError):
        return "Email not sent - connection error"
