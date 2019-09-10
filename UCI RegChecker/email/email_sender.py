import smtplib
from email.message import EmailMessage

FROM = "276870375@qq.com"
TO = "shensheshoua@126.com"
MAIL_HOST = "smtp.qq.com"
MAIL_USER = "276870375@qq.com"
MAIL_PASS = "hbtdkqzwjryqbjci"

def sendEmail(subject, content, sender = FROM, receiver = TO):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        s = smtplib.SMTP()
        s.connect(MAIL_HOST, 25)
        s.login(MAIL_USER, MAIL_PASS)
        s.send_message(msg)
        print("Succeeded")
    except smtplib.SMTPException as e:
        print("Failed. Error: " + e)
    finally:
        s.quit()

