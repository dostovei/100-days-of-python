programming_dictionary = {
  "Bug": #key
  "An error in a program that prevents the program from running as expected.", #value
  "Function": #key 
  "A piece of code that you can easily call over and over again.", #value
}
# PYTHON DICTIONARIES

# {Key: Value}

# Retrieving items from dictionary.
# print(programming_dictionary["Bug"]) # watch for types with the Key, yields KeyError

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary["Loop"])

# Start with an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {} 
# print(programming_dictionary)

# Edit item in dictionary
programming_dictionary["Bug"] = "A moth inside your computer."
# print(programming_dictionary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
  print(key) # loop only gives you the KEYS in programming_dictionary
  print(programming_dictionary[key]) # loops and prints both the keys and their values.