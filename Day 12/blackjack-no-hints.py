import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = random.sample(cards, 2)
player_hand = random.sample(cards, 2)
current_score = sum(player_hand)
dealer_score = sum(dealer_hand)
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
print(logo)
def deal_cards():
  if play_game == "y":
    dealer_first_card = dealer_hand[0]
    print(f"  Your cards: {player_hand}, current score: {current_score}")
    print(f"  Computer's first card: {dealer_first_card}")
    
    another_card = True

    while another_card:
      if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
        another_player_card = random.choice(cards)
        player_hand.append(another_player_card)
        new_current_score = sum(player_hand)
        
        # final_dealer_hand = dealer_hand + second_dealer_card
        print(f"  Your cards: {player_hand}, current score: {new_current_score}")
        print(f"  Computer's first card: {dealer_first_card}")
        if sum(player_hand) < 22:
          dealer_new_cards = random.choice(cards)
          dealer_hand.append(dealer_new_cards)
          print(f"  Your cards: {player_hand}, current score: {new_current_score}")
          print(f"  Computer's first card: {dealer_hand}")
          print(f"  Your final hand: {player_hand}, final score: {new_current_score}")
          print(f"  Computer's final hand: {dealer_hand}, final score: {dealer_score}")
        else:
          print(f"  Your cards: {player_hand}, current score: {new_current_score}")
          print(f"  Computer's first card: {dealer_hand}")
          print(f"  Your final hand: {player_hand}, final score: {new_current_score}")
          print(f"  Computer's final hand: {dealer_hand}, final score: {dealer_score}")
          print("You went bust!")
          deal_cards()
      else:    
        print(f"  Your final hand: {player_hand}, final score: {current_score}")
        print(f"  Computer's final hand: {dealer_hand}, final score: {dealer_score}")
        if current_score > dealer_score:
          print("You win!")
          deal_cards()
        else:
          print("You lose!")
    else:
      deal_cards()
    
        # print(final_dealer_hand)
      
      

deal_cards()

