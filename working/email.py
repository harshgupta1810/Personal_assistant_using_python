import smtplib


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('desperateenuf52@gmail.com', '1810@harsh')
    server.sendmail('desperateenuf52@gmail.com', to, content)
    server.close()