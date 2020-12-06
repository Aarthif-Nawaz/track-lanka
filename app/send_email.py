## importss
import smtplib
from email.message import EmailMessage
from app.config import EMAIL_ADDRESS,PASSWORD


def send_email(to,subject,body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg.set_content(body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS,PASSWORD)
        smtp.send_message(msg)
        print("Successfully Sent Email ! ")
