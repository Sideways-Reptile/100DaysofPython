**DAY 5 - Lists**

Today's lesson taught me a lot about lists and how to take input from a User
and use that as a parameter for a Range function. in this case, the user tells us
how many Numbers, letters and symbols they want in their password. the code then
iterates through the provided lists and randomly selects the right number of 
options and appends them to another list which will be the Password.

There were two version to this challenge, Hard mode is posted and Easy mode is below:
    
    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
     passwordList = []
     password = ""
     for char in range(1, nr_letters + 1):
       passwordList.append(random.choice(letters))
    
     for symbol in range(1, nr_symbols + 1):
       passwordList.append(random.choice(symbols))
    
     for number in range(1, nr_numbers + 1):
       passwordList.append(random.choice(numbers))
    
     for i in passwordList:
       password += i
    
     print(password)

Hard Mode introduced the Random module and its feature of Shuffle. I was able
to simply shuffle the order of the list created before converting to a string and
presenting to the User.