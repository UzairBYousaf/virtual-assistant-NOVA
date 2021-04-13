import smtplib
from ss import *

def sendEmail():
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, epwd)
    server.sendmail(senderEmail,reciever,'Hello! This is a test e-mail by Nova')
    server.close()