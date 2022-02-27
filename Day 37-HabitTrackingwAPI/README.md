# Habit tracking

this challenge uses more APIs to help create an App that tracks your habits using a neat
tool called Pixela. This will create a Visual representation of how
one makes progress with a habit. intensity settings included. 

The main focs of this challenge is getting familiar with the other elements of the
Requests module like .POST, .PUT, and .DELETE. 

- Post is for posting data to a system; uses 'json' instead of 'params' like with GET
- Put is for updating/editing data on that system
- Delete is for deleting data from a system
- Get is used to ask for data from a system

#### HTTP Headers
Part that contains the relevant info regarding who/what/where this data came from.
Can set up Auth tokens for APIs using HTTP Headers. This is the preferred method
as it helps keep Tokens out of Code and uploaded to public spaces, and protected from sniffers.

Can use datetime module to tap into the strftime module to format the date string into something
easy to use by the API. I plan to update thi code to have a GUI and help the user more easily
track their habits. Could potentially use an rPi and make this a gift for someone.