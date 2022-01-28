**LISTS**

Learned how lists work. How to call data from indices.
Some basic code:

    states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
    print(states_of_america[12])

    dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
    print(dirty_dozen[5])

Also learned about Random module. The code below as an example:

    import random
    
    coinFlip = random.randint(0, 1)
    if coinFlip == 1:
      print("Heads")
    else:
      print("Tails")
    
    #below produces Rand Num btwn 0.00 - 1.00.
    #Byb * rand.rand by 6, we are extending range to 0.00 - 6.00
    randomFloat = round(random.random() * 6, 3)  #rounds to 3 places
    print(randomFloat)

The final Project for the day was to make a simple Rock, Paper, Scissors game.
There is art included.