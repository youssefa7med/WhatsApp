import tkinter as tk
from tkinter import messagebox
import pywhatkit as kit
import time
from datetime import datetime

def send_message():
    # Get input values
    numbers_input = phone_numbers_entry.get()
    message = message_text.get("1.0", tk.END).strip()
    scheduled_date = date_entry.get_date()
    scheduled_time = time_entry.get_time()

    # Convert the input string into a list of phone numbers and add +20
    phone_numbers = [f"+20{num.strip()}" if not num.startswith("+") else num.strip() for num in numbers_input.split(",")]

    # Send message to each number in the list
    for i, number in enumerate(phone_numbers):
        try:
            # Check if time and date are provided
            if scheduled_date and scheduled_time:
                # Schedule the message
                hour = scheduled_time.hour
                minute = scheduled_time.minute + i  # Add a minute delay for each recipient
                kit.sendwhatmsg(number, message, hour, minute, wait_time=4, tab_close=False)  # Keep the tab open
                log_text.insert(tk.END, f"Message scheduled to {number} at {hour}:{minute}\n")
            else:
                # Send message instantly without wait time
                kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=False)  # Keep tab open
                log_text.insert(tk.END, f"Message sent to {number}\n")

            time.sleep(5)  # Short delay between sending messages to avoid issues

        except Exception as e:
            log_text.insert(tk.END, f"Failed to send message to {number}: {e}\n")

    log_text.insert(tk.END, "Messages processed!\n")

# Create the main window
root = tk.Tk()
root.title("WhatsApp Message Sender")

# Create and place widgets
tk.Label(root, text="Enter phone numbers (comma-separated):").pack()
phone_numbers_entry = tk.Entry(root, width=50)
phone_numbers_entry.pack()

tk.Label(root, text="Enter your message:").pack()
message_text = tk.Text(root, height=5, width=50)
message_text.pack()

tk.Label(root, text="Select the date to schedule the message (optional)").pack()
date_entry = tk.DateEntry(root)
date_entry.pack()

tk.Label(root, text="Select the time to schedule the message (optional)").pack()
time_entry = tk.TimeEntry(root)
time_entry.pack()

send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.pack()

log_text = tk.Text(root, height=10, width=50)
log_text.pack()

# Run the application
root.mainloop()
