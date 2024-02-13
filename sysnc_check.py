#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import time,datetime

def send_mail(info):

    smtp_server = 'smtp.163.com'
    smtp_port = 25
    sender_email = 'm18258287538@163.com'
    sender_password = 'XGZAPDCIAVXUMDFH'

    #recipient_email = 'liumao@sugon.com'
    recipient_email = 'm18258287538@163.com'


    message = MIMEText(info, 'plain', 'utf-8')
    message['From'] = "liumao@163.com"
    message['To'] = "liumao@sugon.com"
    message['Subject'] = Header('rsync has err', 'utf-8')

    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.login(sender_email, sender_password)

        smtp_connection.sendmail(sender_email, recipient_email, message.as_string())

        smtp_connection.quit()

        print("mail send successed")

    except Exception as e:
        print("Error for send mail:", e)

if __name__ == '__main__':
    f = "/var/log/rsyncd.log"
    mtime=datetime.datetime.fromtimestamp(os.path.getmtime(f))
    file_mtime=mtime.strftime("%Y-%m-%d %H:%M")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    if file_mtime == now:
        print("File last modified : %s, The System time: %s" % (file_mtime,now))
        send_mail("File last modified : %s, The System time: %s" % (file_mtime,now))
    else:
        print("The file is not equal")
