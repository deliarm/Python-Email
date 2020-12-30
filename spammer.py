"""
References:
https://docs.python.org/3/library/email.examples.html
https://docs.python.org/3/library/smtplib.html
https://realpython.com/python-send-email/
https://www.w3schools.com/python/python_file_open.asp

"""
import getpass
import smtplib

# set server and port for gmail (can change to other mailing domains)
# a few popular mailing domains are listed below:
# outlook: port = 587 , smtp_server = smtp.gmail.com
# outlook: port = 587 , smtp_server = smtp-mail.outlook.com
# yahoo  : port = 465 , smtp_server = smpt.mail.yahoo.com
# hotmail: port = 587 , smtp_server = smtp-mail.outlook.com
smtp_server = 'smtp.gmail.com'
port = 587

# set the recipient and senders emails 
email_user       = '@gmail.com'                         # your email here (gmail by default)
password         = getpass.getpass('Password: ')        # input prompt for your password
email_receiver   = '@gmail.com'                         # the person you want to spam (gmail by default)
subject          = 'Input subject (aka header)'         # change to subject of email
body             = (open("message.txt","r")).read()     # body of email (change in .txt file)
repeat           = input('How many emails?: ')          # the amount of times the message will send

try:

    # create and login to server using your account
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    server.starttls()
    server.login(email_user,password)
    print("\nSending To : " + email_receiver)

    # send the email in a for loop , 'repeat' amount of times
    for i in range(int(repeat)):
        msg = 'From: ' + email_user + '\nSubject: ' + subject + '\n' + body  # prepare message
        server.sendmail(email_user,email_receiver,msg)                       # send the email
        print("\rEmail Sent - " + str(i+1) )                                 # email sent confirmation

    server.quit()                                       # quit the server (sign out)
    print("\n",repeat,"Email(s) sent successfully \n")  # notify user of successful email


# if a secure connection is not established print the following
except smtplib.SMTPAuthenticationError:
    print("\nError - Authentication error, incorrect username and/or password")
    sys.exit()
