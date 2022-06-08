from email import message
from http import server
import smtplib
try:
    sender_email = "rahulkumarthakurofficial123@gmail.com"
    reciver_email = "rahulthakur2057@gmail.com"
    password = ""
    message = "this message is for testing my program."

    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,password)
    print("successful!!!")
    server.sendmail(sender_email,reciver_email,message)
    print("sent to",reciver_email)
    server.quit
except:
    print("ask to sir")