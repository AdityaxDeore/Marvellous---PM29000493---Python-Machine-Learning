import schedule
import time
import os
from datetime import datetime

def CreateLog():
    now = datetime.now()
    # Format: MarvellousLog_25_07_2026_16_30_00.txt
    filename = now.strftime("MarvellousLog_%d_%m_%Y_%H_%M_%S.txt")
    
    try:
        with open(filename, 'w') as fd:
            fd.write("Log file created successfully.\n")
            # Format: Creation Time: 25-07-2026 04:30:00 PM
            creation_time = now.strftime("%d-%m-%Y %I:%M:%S %p")
            fd.write(f"Creation Time: {creation_time}\n")
        print(f"Log file created: {filename}")
    except Exception as e:
        print(f"Error creating log file: {e}")

def main():
    print("Application started... Press Ctrl+C to stop.")
    
    # Schedule to run every 10 minutes
    schedule.every(10).minutes.do(CreateLog)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nApplication stopped.")

if __name__ == "__main__":
    main()
