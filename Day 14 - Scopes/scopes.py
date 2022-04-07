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

# There is NO Block Scope in Python
# Example:
game_level = 3
def create_enemy():  
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]
  print(new_enemy) # has to indent inline with if statement

create_enemy()

# ^^^^^^^^^^^^^^^^
# if, while and for code blocks DO NOT CREATE LOCAL SCOPES

# Modifying Global Scope
# Not Recommended in Python
enemies = 1

def increase_enemies():
  global enemies  # YOU DON'T NORMALLY WANT TO DO THIS, CAN CAUSE BUGS
  enemies += 1 
  print(f"enemies inside function: {enemies}")

# INSTEAD, DO THIS

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants
PI = 3.14159 
URL = "https://www.google.com"    # Global constants should always be named with all CAPITALS
TWITTER_HANDLE = "@returnRyan"