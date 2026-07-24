# Duplicate File Removal Automation

## Project Description

This script periodically scans a specified directory, detects duplicate files
using MD5 checksums, deletes the duplicate copies (keeping one original file
per duplicate group), creates a detailed timestamped log file, and sends the
log file to a receiver through email. Scanning repeats automatically after the
configured time interval until the script is terminated manually.

## Features

- Recursive directory scanning (including subdirectories)
- Checksum-based duplicate detection (MD5 of file content, not file names)
- Automatic duplicate-file deletion (first file of each group is preserved)
- Timestamp-based log generation inside the `Marvellous` directory
- Periodic execution after a configurable time interval (in minutes)
- Email notification with the log file attached
- Operation statistics included in the email body
- Full input validation (directory, interval, email, command-line arguments)
- Robust exception handling (missing files, permission errors, email failures)
- Modular programming (all helper functions in `duplicate_utils.py`)
- Help (`--help`) and Usage (`--usage`) options

## Requirements

- Python 3.8 or higher
- Standard library only: `hashlib`, `os`, `re`, `smtplib`, `datetime`,
  `email`, `sys`, `time` (no third-party packages needed)
- Internet connection for sending email
- Email application password (or SMTP credentials) for the sender account

## Project Structure

- `DuplicateFileRemoval.py` — main automation script; parses command-line
  arguments, validates input, drives the periodic scan-delete-log-email cycle
- `duplicate_utils.py` — user-defined module containing every helper function:
  `display_help`, `display_usage`, `validate_directory`, `validate_interval`,
  `validate_email`, `create_log_directory`, `create_log_file`, `write_log`,
  `calculate_checksum`, `scan_directory`, `find_duplicates`,
  `delete_duplicates`, `build_email_body`, `send_email`
- `Marvellous/` — directory created at runtime in the current working
  directory; stores all generated log files

## Command-Line Options

| Argument | Description |
|---|---|
| `<AbsoluteDirectoryPath>` | Absolute path of the directory to scan |
| `<TimeIntervalInMinutes>` | Scan interval in minutes (numeric, greater than zero) |
| `<ReceiverEmailAddress>` | Email address that receives the log file |
| `--help` | Display the help screen |
| `--usage` | Display the usage line |

## Execution Command

```bash
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
```

## Help Command

```bash
python DuplicateFileRemoval.py --help
```

## Usage Command

```bash
python DuplicateFileRemoval.py --usage
```

Expected output:

```text
Usage: python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>
```

## Log-File Information

- Logs are stored in the `Marvellous` directory, created in the current
  working directory (an existing directory is reused).
- Log file names contain the creation date and time:
  `DuplicateRemovalLog_DD_MM_YYYY_HH_MM_SS.log`
  (example: `DuplicateRemovalLog_20_07_2026_23_30_15.log`).
- Each log file records: starting time of scanning, completion time of
  scanning, name of the scanned directory, total files scanned, duplicate
  files found, duplicate files deleted, checksum values of duplicate groups,
  complete paths of all deleted files, errors encountered, and email delivery
  status.

## Email Configuration

- The sender email and app password are read from the environment variables
  `SENDER_EMAIL` and `SENDER_APP_PASSWORD`.
- For Gmail, generate an App Password (Google Account → Security → 2-Step
  Verification → App passwords) and use it instead of your login password.
- Do not hard-code real credentials in the source code.

```bash
export SENDER_EMAIL="your_email@gmail.com"
export SENDER_APP_PASSWORD="your_app_password"
```

## Important Notes

- Deleted files may not be recoverable — first test on a sample directory.
- The first file from each duplicate group is preserved; only the remaining
  copies are deleted.
- Files are considered duplicates only when their checksums are identical
  (same content), never by name alone.
- Email passwords should never be hard-coded; use environment variables.
- If email sending fails (no internet, bad credentials), the failure is
  recorded in the log and the script continues; it never crashes.
- The script runs until it is manually terminated (Ctrl+C).
