import ssl
import certifi
import smtplib

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "hermusme07@gmail.com"
    password = "qczr gjws zodu hlug"   
    receiver = "newsappflask4@gmail.com".strip()

    
    context = ssl.create_default_context(cafile=certifi.where())

    subject = "Tesla News"
    email_message = (
        f"Subject: {subject}\n"
        f"From: {username}\n"
        f"To: {receiver}\n\n"
        f"{message}"
    )

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message)
