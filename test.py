import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Streamlit UI
st.title("Selenium WebDriver with Local Chrome")
st.write("Launching Chrome browser...")

# Setup Chrome options for headless mode
options = Options()
options.add_argument('--headless')  # Run in headless mode (no GUI)
options.add_argument('--no-sandbox')  # Required for running as root
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

# Setup Chrome WebDriver using webdriver_manager
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.saucedemo.com")
    st.write("Page title:", driver.title)
except Exception as e:
    st.error(f"An error occurred: {e}")
finally:
    # Close the WebDriver
    driver.quit()
