############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 20):  # for loops omit the stop (20), **change 20 to 21**
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # lists are indexed starting at 0, so (1, 6) should be (0, 5)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994: # elif statement does not include 1994, change to year >= 1994
  print("You are a Gen Z.")

# Fix the Errors
age = input("How old are you? ")
if int(age) > 18:
  print(f"You can drive at age {age}.")

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # == should be =
total_words = pages * word_per_page # can't concatenate str, must be int(pages * word_per_page)
print(total_words)

# #Use a Debugger
# https://pythontutor.com/visualize.html#mode=edit
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item) # does not append list because it is outside the for loop, NEEDS INDENTED ONCE
  print(b_list)

mutate([1,2,3,5,8,13])