import smtplib
import ssl
import csv
from email.mime.text import MIMEText
from time import sleep

port = 587  # Port of outlook office 365
smtp_server = "smtp.office365.com"  # Put here your mail domain service
sender_email = input("Put here your mail adress")
password = input("Put here your password")


# Function to access to the server mail and send the message
def send_email():
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


# Read the csv and write the mail components
with open('emails.csv', newline='', encoding='latin-1') as csvfile:
    context = ssl.create_default_context()
    reader = csv.DictReader(csvfile)
    for row in reader:
        receiver_name = row['Name']
        receiver_email = row['Email']
        message = f"""\
        Hi {receiver_name}, \n
        ...

        """
        msg = MIMEText(message)
        msg['From'] = sender_email
        msg['Cc'] = ''
        msg['Subject'] = ''
        send_email()
        sleep(1)
csvfile.close()

