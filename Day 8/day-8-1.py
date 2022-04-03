# Review: 

# Create a function called greet(). 
def greet():
  # Write 3 print statements inside the function.
  print("Hello.")
  print("How do you do?")
  print("Goodbye.")
# Call the greet() function and run your code.
greet()

# FUNCTIONS WITH INPUTS
# def my_function(something):
  #do this with something:
  #then do this
  #finally do this
# my_function(123) --- passes variable 123 through my_function
# something = 123 now

#Function that allows for input

def greet_with_name(name):
  print(f"Hello {name}.")
  print(f"How do you do, {name}?")  #  name is called the **parameter**
  print(f"Goodbye, {name}")         #  "Ryan" is called the **argument**
                                    #  name = "Ryan"
greet_with_name("Ryan")


# FUNCTIONS WITH MORE THAN 1 INPUT

def greet_with(name, location): # name AND location are both parameters
  print(f"Hello {name}.")
  print(f"What is it like in {location}?")
greet_with("Ryan", "Ohio")  
# arguments are assigned in the order of their parameters
# CALLED A POSITIONAL ARGUMENT
greet_with("Ohio", "Ryan") # would change {name} to Ohio and {location} to Ryan

KEYWORD ARGUMENTS
def my_function(a, b, c):
  #Do this with a
  #Then do this with b
  #Finally do this with c
my_function(a=1, b=2, c=3) # this method forces the arguments to stay with their respective parameters
my_function(c=3, a=1, b=2) # would yield the same results as the above my_function if called

greet_with(name="Ryan", location="Ohio") # KEYWORD ARGUMENT FOR greet_with function