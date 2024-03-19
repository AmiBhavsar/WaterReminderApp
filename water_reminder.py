import tkinter as tk
from datetime import datetime, timedelta
import time

def start_reminder():
    while True:
        current_time = datetime.now()
        next_reminder_time = current_time + timedelta(minutes=30)
        
        while datetime.now() < next_reminder_time:
            time.sleep(60)  # Sleep for 1 minute before checking again
        
        remind_window = tk.Toplevel()
        remind_window.title("Drink Water!")
        reminder_label = tk.Label(remind_window, text="It's time to drink water!")
        reminder_label.pack()
        remind_window.after(5000, remind_window.destroy)  # Close reminder window after 5 seconds

def create_gui():
    root = tk.Tk()
    root.title("Water Reminder")
    
    label = tk.Label(root, text="Stay Hydrated! Drink Water Every 30 Minutes.")
    label.pack()
    
    start_button = tk.Button(root, text="Start Reminder", command=start_reminder)
    start_button.pack()
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
