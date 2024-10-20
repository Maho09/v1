#intro:

- This script sends whatsapp messeges and emails
- You can load data from excel or csv file

"""
driver = webdriver.Chrome(
service=Service("/usr/bin/chromedriver"), options=chrome_options
)#(change path to the location of your ChromeDriver)
"""

- U need to change this part to include the path to chromedriver on your machine

"""
send_email(sender_email, password, receiver_email, msg):
"""

- the password is the app password of your email not the login password

"""
load_file(file)
"""

- pass the path to the excel file you want to read its data

"""
load_csv_file(file)
"""

- pass the path to the csv file you want to read its data
