# <U>SMTP/DateTime Module</u>

## SMTP(smtplib)
Python has a module that makes use of the SMTP protocol to send
emails to people based on whatever criteria we put in. To set up
a basic connection, the code is as follows:

    with smtplib.SMTP("protonmail.smtp.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"

We can open a connection in a similar way to opening files. We first set the connection
with the '.SMTP' class and use your emails SMTP server as string value and set that to a 
variable called Connection. '.starttls' will provide TLS encryption on our message; 
'.login' requires the email we intend to use and the password for that email account;
Lastly, '.sendmail' will send the message and requires a 'from_addr', 'to_addr', and a 'msg'.
Subject tag is obvious, but to send both Subject line and a Body, tag the subject then place
two New Line symbols and start the body.

## DateTime (datetime)
This module is built-in and doesnt require downloading. Can be imported seperately as a 
variable to make calling a bit less confusing: ('from datetime import datetime')
    
    datetime.datetime.now() - Will get the current time in Yr, Mo, Day, Hr, Sec, Msec,
    datetime.now() - Same output but less typing.

Can also set to a variable that will allow us to access different parts of the method.
   
    today = datetime.now()
    today_tuple = (today.month, today.day)

### Thoughts
This project had me using new techniques like smtp and datetime while also pulling from what 
I have previously learned concerning Pandas, Dict_Comprehension, File/String manipulation.
Most things made sense but the DT module is a bit confusing and I realize that I didnt fully
understand what needed doing for Dict_Comprehension. 