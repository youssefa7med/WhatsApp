import streamlit as st
import pywhatkit as kit
from datetime import datetime
import time

st.set_page_config(page_title="WhatsApp", page_icon="💬")

# Streamlit app
st.title("WhatsApp Message Sender")

# Input phone numbers (take input as a comma-separated string)
numbers_input = st.text_input("Enter phone numbers (comma-separated):", "01000139417")

# Input message
message = st.text_area("Enter your message:", "Hello! This is an automated message.")

# Input scheduled date and time (optional)
scheduled_date = st.date_input("Select the date to schedule the message (optional)", value=None)
scheduled_time = st.time_input("Select the time to schedule the message (optional)", value=None)

# Function to close the browser tab
def close_tab():
    try:
        import pyautogui
        time.sleep(5)  # Short delay to ensure the message is sent
        pyautogui.hotkey('ctrl', 'w')  # Close the tab
    except ImportError:
        st.warning("pyautogui is not available, please close the tab manually.")
    except Exception as e:
        st.error(f"Error closing the tab: {e}")

# When button is clicked
if st.button("Send Message"):
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
                st.write(f"Message scheduled to {number} at {hour}:{minute}")
            else:
                # Send message instantly without wait time
                kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=False)  # Keep tab open
                st.write(f"Message sent to {number}")

            # Close the tab (only if pyautogui is available)
            close_tab()

        except Exception as e:
            st.error(f"Failed to send message to {number}: {e}")

    st.success("Messages processed!")
