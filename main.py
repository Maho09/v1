import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument(
    "--user-data-dir=./User_Data"
)  # Keeps your session logged in

driver = webdriver.Chrome(
    service=Service("/usr/bin/chromedriver"), options=chrome_options
)  # (change path to the location of your ChromeDriver)


# Function to send whatsapp message
def send_whatsapp_message(phone_number, message):
    try:
        driver.get(
            f"https://web.whatsapp.com/send?phone={phone_number}&text={str(message)}"
        )

        send_btn = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p',
                )
            )
        )
        send_btn.click()
        send_btn.send_keys(Keys.ENTER)
        time.sleep(4)
    except Exception as e:
        print("Error sending message to" + phone_number + f"ERROR:{e}")


def send_email(sender_email, password, receiver_email, msg):
    # setting up the email server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        # Set up the server connection
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=30)
        server.starttls()  # Secure the connection

        # Login to email account
        server.login(sender_email, password)

        # Create the email content
        subject = "Notification from Our System"
        body = msg

        # Create a multipart message
        email_msg = MIMEMultipart()
        email_msg["From"] = sender_email
        email_msg["To"] = receiver_email
        email_msg["Subject"] = subject

        # Add the email body
        email_msg.attach(MIMEText(body, "plain"))

        # Convert the message to a string and send it
        text = email_msg.as_string()
        print(f"Sending email to: {receiver_email}")
        server.sendmail(sender_email, receiver_email, text)

        print(f"Email sent successfully to {receiver_email}!")
    except smtplib.SMTPException as smtp_error:
        print(f"Error sending email: {smtp_error}")
    finally:
        server.quit()  # Close the connection


def load_excel_file(file):
    # Read the Excel file into a DataFrame
    if not os.path.exists(file):
        raise FileNotFoundError(f"the file {file} can not be found")
    return pd.read_excel(file)


def load_csv_file(file):
    # Read the Excel file into a DataFrame
    if not os.path.exists(file):
        raise FileNotFoundError(f"the file {file} can not be found")
    return pd.read_csv(file)
