# Black Jack Game made by Teliucs

############### Blackjack Rules #####################

## The deck is not unlimited in size (52 cards). 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are removed from the deck as they are drawn.

import random
from art import logo


def main():
    print("-------------------------------------------------------------")
    print("""Welcome to the Teliucs Black Jack
    Would you like to play?
        [1] Yes | [2] No""")
    if int(input()) == 1:
        print(logo)
        play()
    else:
        print("I already felt that you were not ready for this.")
    print("-------------------------------------------------------------")


def init_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    
    first_me = random.choice(cards)
    cards.remove(first_me)
    second_me = random.choice(cards)
    cards.remove(second_me)
    first_computer = random.choice(cards)
    cards.remove(first_computer)
    second_computer = random.choice(cards)
    cards.remove(second_computer)
    
    my_cards = [first_me, second_me]
    computer_cards = [first_computer, second_computer]
    
    return cards, my_cards, computer_cards


def play():
    """Start, play and end game"""
    cards, my_cards, computer_cards = init_cards()
    my_score = sum(my_cards)
    computer_score = sum(computer_cards)
    
    print(f"Your cards: {my_cards}, score: {my_score}.")
    print(f"Compter's first card: {computer_cards[0]}.")
    print()

    print("\tDo you want another card or to pass?")
    choice = int(input("\t[1] Yes | [2] Pass: "))
    
    i = 1
    while choice == 1:
        print()
        print(f"\tTURN {i}:")
        cards, my_cards, my_score = draw_cards(cards, my_cards, my_score)
        print(f"\tYour cards: {my_cards}, score: {my_score}.")
        print(f"\tCompter's first card: {computer_cards[0]}.")
        print()
        print("\tDo you want another card or to pass?")
        choice = int(input("\t[1] Yes | [2] Pass: "))
        i += 1

    


def draw_cards(cards, my_cards, my_score):
    mine = random.choice(cards)
    print(f"\tYou have drawn {mine}.")
    cards.remove(mine)
    if mine == 11:
        mine = choose_value_ace()
    my_cards.append(mine)
    my_score = sum(my_cards)
    if my_score > 21:
        print(f"\tYou have exceed the maximum value, now you are at {my_score}. Sorry you have just lost.")
    return cards, my_cards, my_score


def calculate_results(my_score, comp_score):
    pass


def choose_value_ace():
    print()
    print("\t\tGiven that you have drawn an ace, you have to choose its value.")
    choice = int(input("\t\t[1] | [11]: "))
    while choice != 1 and choice != 11:
        print("\t\tYou have to choose between 1 and 11.")
        choice = int(input("\t\t[1] | [11]: "))
    if choice == 1:
        return 1
    else:
        return 11
    
    

if __name__ == '__main__':
    main()