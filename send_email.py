import smtplib, ssl
from generate_message import message

def send():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = ""
    receiver_email = ""
    password = "" # password for the sender mail is necessary for this process
    msg = message()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        #server.ehlo()  # Can be omitted
        server.starttls(context=context)
        #Wserver.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)