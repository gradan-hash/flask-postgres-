import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = os.getenv("Login")
    password = os.getenv("Password")
    message = f"<h3>Feedback submission</h3><ul><li>Customer : {customer}</li><li>dealer : {dealer}</li><li>rating : {rating}</li><li>comments : {comments}</li></ul>"

    send_email = "corneliusmutuku55@gmail.com"
    receiver_email = "corneliusmutuku55@gmail.com"
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'lambo feedback'
    msg['From'] = send_email
    msg['To'] = receiver_email

    # send email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(send_email, receiver_email, msg.as_string())
