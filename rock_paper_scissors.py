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

#Write your code below this line 👇
import random
random_integer = random.randint(0,2)
choice2 = random_integer

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print(rock)
  print("Computer chose:")
elif choice == 1 :
  print(paper)
  print("Computer chose:")
elif choice == 2 :
  print(scissors)
  print("Computer chose:")
else:
  print("Computer chose:")

if choice2 == 0:
  print(rock)
if choice2 == 1 :
  print(paper)
if choice2 == 2 :
  print(scissors)
if choice == 0 and choice2 == 2:
  print("you Win.")
elif choice == 2 and choice2 == 1:
  print("You Win.")
elif choice == 1 and choice2 == 0:
  print("You Win.")
elif choice2 == 0 and choice == 2:
  print("You lose.")
elif choice2 == 2 and choice == 1:
  print("You lose.")
elif choice2 == 1 and choice == 0:
  print("You lose.")
elif choice == choice2:
  print("Draw")
else:
  print("Invalid number.You Lose!")


