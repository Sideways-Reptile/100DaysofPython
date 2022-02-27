import smtplib

MY_EMAIL = "Sidewaays666@gmail.com"
MY_PASSWORD = "Rq5fw5kqpQmXdUm"
# SMS_GATEWAY = "+18316822168@vtext.com"
smtp = "smtp.gmail.com"

with smtplib.SMTP(smtp, 587) as connection:
    connection.starttls()
    connection.login(
        user=MY_EMAIL,
        password=MY_PASSWORD
    )
    connection.sendmail(
        to_addrs="impressive-tie@pm.me",
        from_addr=MY_EMAIL,
        msg=f"Subject: Testing!\n\nTesting text functionality."
    )
