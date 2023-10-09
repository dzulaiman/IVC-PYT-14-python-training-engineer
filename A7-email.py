#!/usr/bin/env python
#Email module
#dzul.aiman@gmail.com
#2023-10-09

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
password = "your_email_password"
subject = "Test Email from Python"
message = "This is a test email sent from Python."

# Create a MIMEText object to represent the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))

# Establish a secure session with Gmail's outgoing SMTP server using SSL
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
