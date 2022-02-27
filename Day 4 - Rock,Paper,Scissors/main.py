import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
playerChoice = int(input("what do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors.\n"))

print("Player's Choice")
if playerChoice >= len(options) or playerChoice < 0:
    print("You've entered an invalid option, you Lose!")
else:
    print(options[playerChoice])

    print("Computer's Choice")
    computerChoice = random.randint(0, 2)
    print(options[computerChoice])

    # Scoring
    # rock > scissors
    # paper > rock
    # scissors > paper

    if playerChoice == 0 and computerChoice == 2:
        print("You Win!")
    elif playerChoice == 2 and computerChoice == 0:
        print("You Lose!")
    elif playerChoice < computerChoice:
        print("You Lose!")
    elif playerChoice == computerChoice:
        print("It's a Draw!")
    else:
        print("You Win!")


