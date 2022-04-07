################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion() # prints 2
# print(drink_potion) # NameError, 'potion_strength' is not defined.

# Global Scope

player_health = 10 # global variable
def game():
  def drink_potion():
    potion_strength = 2
    print(player_health)

  drink_potion() # drink_potion() is indented enough to be within the local scope of def drink_potion(), so it works when called.

# Namespace == anything I give a name to. ie variables, functions, etc