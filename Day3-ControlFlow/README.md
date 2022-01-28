Todays lesson showed me how to Control the flow of the program using logical operators.
The main project for today, a Choose Your Own Adventure type, was meant to demonstrate the power of If/Else/elif statement
and how these can be used to help direct the flow of logical traffic through the program.

Much of this stuff I still remember form that college course I took. 
Would probably be a good Idea to find that code and push it up to git like this code.

Most of the exercises were forked from replit. Some examples include:

    #If,else,elif, Nested if/else
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    bill = 0
    
    if height >= 120:
      print("You can ride the rollercoaster!")
      age = int(input("What is your age? "))
      if age < 12:
        bill = 5
        print("Child tickets are $5.")
      elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
      elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
      else:
        bill = 12
        print("Adult tickets are $12.")
      
      wants_photo = input("Do you want a photo taken? Y or N. ")
      if wants_photo == "Y" or wants_photo == "y":   #without OR statement, inputting 'y' will result in No Charge being added for photo.
        bill += 3
      
      print(f"Your final bill is ${bill}")
    
    else:
      print("Sorry, you have to grow taller before you can ride.")


In addition to the Pizza Calculator which detailed further
multiple if/else statements:

    # 🚨 Don't change the code below 👇
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")
    # 🚨 Don't change the code above 👆
    
    #Write your code below this line 👇
    bill = 0.00
    
    if size == "S" or size == "s":
      bill += 15
    elif size == "M" or size == "m":
      bill += 20
    elif size == "L" or size == "l":
      bill += 25
    else:
      print("Not a Valid size.")
    
    if add_pepperoni == "Y":
      if size == "S":
        bill += 2
      elif size != "M" and size != "m" and size != "L" and size != "l" :
        print("What size you want?!") 
      else:
        bill += 3
    elif add_pepperoni != "N":
      print("It's a yes or no.")
    
    if extra_cheese != "Y":
      if extra_cheese != "N":
        print("I'm done...")
        bill += 35
    else:
      bill += 1
    
    total_Bill = "{:.2f}".format(bill)
    print(f'Your final bill is ${total_Bill}.')




