# RANDOMISATION
# Mersenne Twister - Python's pseudorandom number generator (PNG) - See video on Khan Academy

# askpython.com >>> python random module


import random 
# uses pythons randomisation module
# import my_module
# imports the module my_module.py that I created

# print(my_module.pi)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)
# random.random() generates a random FLOAT number between 0.0 and 1.0 (never 0.0 nor 1.0, however)

random_float_two = random.random() * 5
print(random_float_two)
# multiplying random.random() by 5 stretches our range from 0.0-5.0, instead of 0.0-1.0

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")