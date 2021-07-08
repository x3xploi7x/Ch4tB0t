###
#   Author : ExploitNetwork
#   Version : 1.2.1
#   Languaje : python
###

import smtplib
from os import environ

message = 'YOURE SYSTEM IS EXPOSED'
subject = 'HACKYOU'
message = 'Subject: {}\n\n{}'.format(subject, message)

sender = environ.get('EMAIL_SENDER')
password = environ.get('MY_PASSWORD_PRIV')
transmitter = environ.get('EMAIL_TRANSMITTER')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)

server.sendmail(sender, transmitter, message)
server.quit()

print('Mail Sent SuccessFully. . .')
