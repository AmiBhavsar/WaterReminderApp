from datetime import datetime, timedelta
import time
from plyer import notification

def start_reminder():
    while True:
        current_time = datetime.now()
        next_reminder_time = current_time + timedelta(minutes=15)
        
        while datetime.now() < next_reminder_time:
            time.sleep(60)  # Sleep for 1 minute before checking again
        
        notification_title = "Drink Water!"
        notification_message = "It's time to drink water!"
        notification.notify(
            title=notification_title,
            message=notification_message,
            app_icon='glass-of-water-icon.ico', 
            timeout=10,  # Notification will disappear after 10 seconds
            toast=False,  # Disable Windows toast notification style
            app_name='Water Reminder',  # Set the app name for better notification grouping
            # font='Segoe UI Bold',  # Set the font for the notification message
            # app_icon_size=(64, 64)  # Set the icon size (width, height)
        )

def main():
    print("Water Reminder App started.")
    start_reminder()

if __name__ == "__main__":
    main()
