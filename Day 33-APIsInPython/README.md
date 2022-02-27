## Day 32 - API in Python
   
Learned about the 'request' module in python that makes easy work of getting data from an 
API hosted by a service. In this project we looked at how two different APIs work;
**ISS Space Station** and **Sunrise/Sunset Time**.\
The 'request' module allows use to specify the API url to collect data from by simply adding 
'.get' to the request and adding the URL as an option. More complex APIs will allow for 
parameters to be set for the API call, like the code below.

    def is_night():
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
                             
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        time_now = datetime.now().hour
        if time_now >= sunset or time_now <= sunrise:
            return True
We can pre-define the parameters we want and then place them in the call. The response we
get can then be turned into JSON data with '.json()', which can then be used to more easily 
pulled from and worked with.\
The above code allows us to split the data and retrieve the Hour and comparing it with
the current hour of today. based on the if statement, if its nighttime it will return True.
The main difference between this call and the ISS API call is the latter doesnt take any
params.

We later added email functionality to the program by checkin if the ISS was overheard
AND it was nighttime based on my location, then an email will be sent to me to let me know.
This then reinforces what I learned re: SMTP module. 