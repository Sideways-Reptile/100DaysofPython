#Tip Calculator
print("Welcome to the Tip Calculator")
bill = float(input("How much was the total bill? $" ))
tip = int(input("Would you like to leave a 12, 15, or 17 percent tip? "))
split = int(input("Split how many ways? "))


tab_Total = round(tip / 100 * bill + bill, 2)
per_Person = tab_Total / split
final_Amount = "{:.2f}".format(per_Person)
print(f"Your total is ${final_Amount} each.")