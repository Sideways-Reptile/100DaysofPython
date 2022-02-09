import smtplib

MY_EMAIL = "Sidewaays666@gmail.com"
MY_PASSWORD = "Rq5fw5kqpQmXdUm"
smtp = "smtp.gmail.com"


class NotificationManager:
    # def __init__(self):
    #     self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    #
    def __init__(self, emails, message, google_flight_link):
        with smtplib.SMTP(smtp, 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    to_addrs=email,
                    from_addr=MY_EMAIL,
                    msg=f"Subject: New Deals!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
    # def send_sms(self, message):
    #     message = self.client.messages.create(
    #         body=message,
    #         from_=TWILIO_VIRTUAL_NUMBER,
    #         to=TWILIO_VERIFIED_NUMBER,
    #     )
    #     print(message.sid)
