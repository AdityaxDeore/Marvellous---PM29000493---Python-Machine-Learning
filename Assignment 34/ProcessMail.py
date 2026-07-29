"""
Question 4:
Write an automation script named ProcessMail.py that accepts two command line
arguments: receiver's email address and a log file path. The script should send
the specified log file as an attachment to the given email address.

Example: python ProcessMail.py marvellousinfosystem@gmail.com ProcessLog.txt
"""

import os
import smtplib
import sys
from email.message import EmailMessage


def SendLogFile(ReceiverEmail, LogFilePath):
    sender = os.environ.get("SENDER_EMAIL")
    password = os.environ.get("SENDER_APP_PASSWORD")

    if not sender or not password:
        print("Error: set SENDER_EMAIL and SENDER_APP_PASSWORD environment variables")
        return

    if not os.path.isfile(LogFilePath):
        print("Error: log file '" + LogFilePath + "' not found")
        return

    try:
        message = EmailMessage()
        message["From"] = sender
        message["To"] = ReceiverEmail
        message["Subject"] = "Process Log File"
        message.set_content("Please find the process log file attached.")

        log_file = open(LogFilePath, "rb")
        message.add_attachment(log_file.read(), maintype="text", subtype="plain",
                               filename=os.path.basename(LogFilePath))
        log_file.close()

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.send_message(message)
        server.quit()
        print("Log file sent to " + ReceiverEmail + ".")
    except smtplib.SMTPAuthenticationError:
        print("Error: email authentication failed. Check your app password.")
    except (smtplib.SMTPException, OSError):
        print("Error: could not send email")


def main():
    print("AutomationScript Started")

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script sends a log file as an email attachment.")
            print("Use --u for usage.")
            return
        if sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("python ProcessMail.py <ReceiverEmail> <LogFilePath>")
            return

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Use --h or --u for more information")
        return

    receiver = sys.argv[1]
    log_file = sys.argv[2]
    SendLogFile(receiver, log_file)


if __name__ == "__main__":
    main()
