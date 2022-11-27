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
    print("----------------------------------------------------------------")
    print("""Welcome to the Teliucs Black Jack
    Would you like to play?
        [1] Yes | [2] No""")
    if int(input()) == 1:
        print(logo)
        play()
    else:
        print("I already felt that you were not ready for this.")
    print()
    print("----------------------------------------------------------------")


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
    print("----------------------------------------------------------------")

    
    return cards, my_cards, computer_cards


def play():
    """Start, play and end game"""
    while True:
        cards, my_cards, computer_cards = init_cards()
        my_score = sum(my_cards)
        computer_score = sum(computer_cards)
        
        print(f"Your cards: {my_cards}, score: {my_score}.")
        print(f"Computer's first card: {computer_cards[0]}.")
        print()

        print("\tDo you want another card or to pass?")
        choice = int(input("\t[1] Yes | [2] Pass: "))
        
        i = 1
        while choice == 1:
            print("\n----------------------------------------------------------------")
            print(f"\tTURN {i}:")
            cards, my_cards, my_score = draw_cards(cards, my_cards, my_score)
            print(f"\tYour cards: {my_cards}, score: [{my_score}].")
            if my_score > 21:
                print(f"\tYou have exceed the maximum value, now you are at [{my_score}]. Sorry you have just lost.")
                break
    
            print(f"\tComputer's first card: {computer_cards[0]}.")
            print()
            print("\tDo you want another card or to pass?")
            choice = int(input("\t[1] Yes | [2] Pass: "))
            i += 1
        print("----------------------------------------------------------------")

        if my_score <= 21:
            cards, computer_cards, computer_score = computer_turn(cards, computer_cards, computer_score)
            if computer_score > 21:
                print(f"\tComputer has exceed the maximum value, now it is at [{computer_score}]. Congrats you have won.")
            else:
                print("\nLet's who won:")
                if calculate_results(my_score, computer_score) == 'W':
                    print('Congrats you have won.')
                elif calculate_results(my_score, computer_score) == 'L':
                    print('Sorry you have just lost. Better luck next time.')
                else:
                    print("It's a tie.")
        break
                
    


def draw_cards(cards, my_cards, my_score):
    """Draw a card from the remaining ones"""
    mine = random.choice(cards)
    print(f"\tYou have drawn {mine}.")
    cards.remove(mine)
    if mine == 11:
        mine = choose_value_ace()
    my_cards.append(mine)
    my_score = sum(my_cards)
    return cards, my_cards, my_score


def computer_turn(cards, computer_cards, computer_scores):
    """Code the computer turn"""
    print("\n\tNow the computer has to drawn or pass.")
    while computer_scores < 17:
        drawn_card = random.choice(cards)
        if drawn_card == 11:
            drawn_card = 1
        cards.remove(drawn_card)
        computer_cards.append(drawn_card)
        computer_scores = sum(computer_cards)
        print(f"\tComputer have drawn {drawn_card}.")
        print(f"\tComputer cards: {computer_cards}, score: [{computer_scores}].")
    else:
        print(f"\tGiven that the computer is at [{computer_scores}], it will no drawn any card.")
    return cards, computer_cards, computer_scores
            

def calculate_results(my_score, computer_score):
    """"Get results"""
    print(f"Your scores is [{my_score}] and the computer's one is [{computer_score}].")
    print("...")
    print("...")
    if my_score > computer_score:
        return 'W'
    if my_score < computer_score:
        return 'L'
    else:
        return 'T'


def choose_value_ace():
    """Ace's value can be 1 or 11, it let the user to choose"""
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