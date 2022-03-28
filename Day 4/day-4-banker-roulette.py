# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
random_name = random.randint(0,len(names)-1) # len function allows us to get total number of items in list, the -1 is to offset the fact that the index starts at 0
print(f"Looks like {names[random_name]} is going to be buying lunch today!") # prints a random indexed random_name in the name list to see who buys lunch!


