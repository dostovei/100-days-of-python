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

computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))


if user_choice == 0:
  print(rock) 
elif user_choice == 1:
  print(paper)
else:
  print(scissors)

if computer_choice == 0:
  print(rock)
  if user_choice == 0:
    print("You and the computer both chose rock. The game is a tie.")
  elif user_choice == 1:
    print("Your paper has covered the computer's rock. You win!")
  else:
    print("The computer has smashed your scissors with a rock. You lose.")
elif computer_choice == 1:
  print(paper)
  if user_choice == 0:
    print("The computer has covered your rock with a piece of paper. You lose.")
  elif user_choice == 1:
    print("You and the computer have both chosen paper. The game is a tie.")
  else:
    print("You have cut the computer's paper with a pair of scissors. You win!")
else:
  print(scissors)
  if user_choice == 0:
    print("You have smashed the computer's scissors with your rock. You win!")
  elif user_choice == 1:
    print("The computer has cut your piece of paper with it's scissors. You lose.")
  else:
    print("You and the computer have both chosen scissors. The game is a tie.")