# STOCK TRACKER

- Good practice to set private info like API Keys to an Environment variable
and to load these into the project instead of hard coding the values
into the code itself. 
- Data extracted from Stock API is returned as JSON and on of the
dictionaries contains our Daily values. We can tap into this and use some
List Comprehension to convert to a list that we can more easily manipulate.


    new_list = [new_item for item in list]

++ since the "list" in question is actually a dictionary, we can tap
into the .item module to get what we need from the data.