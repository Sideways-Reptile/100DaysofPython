# NOTES

Todays project called for us to set up an API with a weather service 
to let us know the weather for a 12 hour period in the event that it rains.

This was simply a review of API calls and how to create them:
    
    import requests
    repsonse = request.get("endpoint.url", params=parameters)
    response.raise_for_status() #checks for Error codes in http
    data = response.json() #converts to json format for easy use

From here we can do whatever we want with the data we received.
For this project, instead of using the Twilio service and instructed,
I have decided to send myself an email to verify functionality.

        with smtplib.SMTP("protonmail.smtp.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"

Twilio Code for same affect:
    
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="YOUR TWILIO VIRTUAL NUMBER",
            to="YOUR TWILIO VERIFIED REAL NUMBER"
        )
    print(message.status)

The code above is required to work with Free accounts on PythonAnywhere, a cloud based service
that will host and run python code. Requires Import of OS module.