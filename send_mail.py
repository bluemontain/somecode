import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import time,datetime

def send_mail():

    smtp_server = 'smtp.163.com'
    smtp_port = 25
    sender_email = 'm18258287538@163.com'  # 这里替换为您自己的发件人邮箱地址
    sender_password = 'XGZAPDCIAVXUMDFH'  # 这里是你的授权码 非邮箱登录密码

    recipient_email = 'liumao@sugon.com,m18258287538@163.com'


    message = MIMEText('This is test! Hello, World!', 'plain', 'utf-8')
    message['From'] = Header('发件人昵称 <{}>'.format(sender_email), 'utf-8')  
    message['To'] = Header('收件人昵称 <{}>'.format(recipient_email), 'utf-8') 
    message['Subject'] = Header('邮件主题', 'utf-8')  

    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.login(sender_email, sender_password)

    # 发送邮件
        smtp_connection.sendmail(sender_email, recipient_email, message.as_string())

    # 关闭连接
        smtp_connection.quit()

        print("邮件发送成功！")

    except Exception as e:
        print("邮件发送失败：", e)



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

