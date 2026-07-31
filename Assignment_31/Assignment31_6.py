import schedule
import time

def PrintMessage(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def main():
    print("Message Scheduler Started...")
    print("Scheduled tasks:")
    print("- Monday at 9:00 AM: Start your weekly goals")
    print("- Wednesday at 5:00 PM: Review your weekly progress")
    print("- Friday at 6:00 PM: Weekly work completed")
    print("Press Ctrl+C to exit.")

    schedule.every().monday.at("09:00").do(PrintMessage, msg="Start your weekly goals")
    schedule.every().wednesday.at("17:00").do(PrintMessage, msg="Review your weekly progress")
    schedule.every().friday.at("18:00").do(PrintMessage, msg="Weekly work completed")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")

if __name__ == "__main__":
    main()
