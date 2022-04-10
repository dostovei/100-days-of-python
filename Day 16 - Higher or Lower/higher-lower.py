from art import logo, vs
from game_data import data
import random
from replit import clear

celeb_a = random.choice(data)
celeb_b = random.choice(data)
celeb_a != celeb_b
follower_count_a = celeb_a["follower_count"]
follower_count_b = celeb_b["follower_count"]


def game(celeb_a, celeb_b):
  score = 0
  print(logo)
  print("Compare A: ", celeb_a["name"], ", a", celeb_a["description"], " from ", celeb_a["country"],".")
  print(vs)
  print("Against B: ", celeb_b["name"], ", a", celeb_b["description"], " from ", celeb_b["country"],".")
  a_or_b = input("Who has more followers? Type 'A' or 'B': ").lower()
  for choice in a_or_b:
  # if/else if user chooses A
    if choice == "a":
      if int(follower_count_a) > int(follower_count_b):
        score += 1
        clear()
        new_celeb_a = celeb_a
        new_celeb_b = random.choice(data)
        new_celeb_a != new_celeb_b
        print(f"You're right! Current score: {score}")
        game(new_celeb_a, new_celeb_b)
      else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
  # if/else if user chooses B    
    if choice == "b":
      if int(follower_count_b) > int(follower_count_a):
        score += 1
        clear()
        new_celeb_a = celeb_b
        new_celeb_b = random.choice(data)
        new_celeb_a != new_celeb_b
        print(f"You're right! Current score: {score}")
        game(new_celeb_a, new_celeb_b)
      else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")

game(celeb_a, celeb_b)
  


