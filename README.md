# Python-Email-Spammer

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

What things you need to install and how to install them

```
Python version 3.0 or higher
smtp package 
```

To install simple mail transfer protocol (SMTP), type the following in your windows command prompt

```
pip install smtp
```
It should look like this,

![image](https://user-images.githubusercontent.com/52977770/103324070-0558e000-4a03-11eb-82ae-0241f8ef8e71.png)

You now have the required software to run the script. Download the repository to your local machine and change lines 22 and 24.
These lines are the sender and receiver emails, respectively. 

#### Before You can Send

The email used to send the spam messaged must change the following security setting.

Click your profile icon (top right of the google page) -> Manage your Google Account -> Security -> Less secure app access

Set this to "On" , if this is not on a secure connection cannot be made (due to built in security features of google).
It should look like this,

![image](https://user-images.githubusercontent.com/52977770/103324157-608ad280-4a03-11eb-92f9-34614c8440ec.png)


Now we are ready to execute in the command line. Make your way to the directory where the repository is downloaded and type
the following command:

```
python spammer.py
```

You will then be prompted to type your password for the email you declared on line 22, you will then input the amount of times
you wish to send the email (max is 10,000 per day on gmail). Here is what a successful execution looks like:

![image](https://user-images.githubusercontent.com/52977770/103324262-02122400-4a04-11eb-8cea-69b02483bfdc.png)

If you would like to change the subject (aka header) of the email you can do so in line 25 of the script. You can also change the body of the email
in the 'message.txt' file .

### Disclaimer:
I am not responsible for anything you do with this script, it is designed solely for learning purposes

### References

https://docs.python.org/3/library/email.examples.html

https://docs.python.org/3/library/smtplib.html

https://realpython.com/python-send-email/

https://www.w3schools.com/python/python_file_open.asp

