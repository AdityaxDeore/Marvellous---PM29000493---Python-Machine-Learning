import sys
import os
import schedule
import time
from datetime import datetime

def CountFiles(dir_path):
    now = datetime.now()
    log_file = "DirectoryCountLog.txt"
    
    if not os.path.exists(dir_path):
        print(f"Error: Directory '{dir_path}' does not exist.")
        return
        
    if not os.path.isdir(dir_path):
        print(f"Error: '{dir_path}' is not a directory.")
        return
        
    try:
        file_count = 0
        for item in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, item)):
                file_count += 1
                
        with open(log_file, 'a') as fd:
            fd.write(f"Directory path: {os.path.abspath(dir_path)}\n")
            fd.write(f"Number of files: {file_count}\n")
            fd.write(f"Date and time: {now.strftime('%d-%m-%Y %H:%M:%S')}\n")
            fd.write("-" * 50 + "\n")
            
        print(f"Logged count for '{dir_path}': {file_count} files at {now.strftime('%d-%m-%Y %H:%M:%S')}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Application started... Press Ctrl+C to stop.")
    
    if len(sys.argv) != 2:
        print("Usage: python Assignment31_5.py <Directory_Name>")
        return
        
    dir_path = sys.argv[1]
    
    # Run once initially
    CountFiles(dir_path)
    
    # Schedule to run every 5 minutes
    schedule.every(5).minutes.do(CountFiles, dir_path=dir_path)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nApplication stopped.")

if __name__ == "__main__":
    main()
