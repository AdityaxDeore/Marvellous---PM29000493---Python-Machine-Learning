import schedule
import time
import datetime

def DisplayMessage(message):
    print(f"[{datetime.datetime.now()}] {message}")

def main():
    message = input("Enter the message to display: ")
    
    interval_input = input("Enter execution interval in seconds (default 5): ").strip()
    if not interval_input:
        interval = 5
    else:
        try:
            interval = int(interval_input)
        except ValueError:
            print("Invalid input! Interval must be an integer.")
            return

    # Validate that the interval is greater than zero
    if interval <= 0:
        print("Error: Interval must be greater than zero.")
        return

    print(f"Scheduling '{message}' every {interval} second(s). Press Ctrl+C to exit.")
    
    # Schedule the function using schedule.every(interval).seconds.do(DisplayMessage, message)
    schedule.every(interval).seconds.do(DisplayMessage, message)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped by user.")

if __name__ == "__main__":
    main()
