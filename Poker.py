#code by The Legendary MlgEpicCar
from random import randint

def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

def convert_card(card: int) -> str:
    """
    A helper function that turns a card value into a string for the player
    """
    if 10 <= card <= 14:
        card = str(card)
        card = card.replace("10", "X")
        card = card.replace("11", "J")
        card = card.replace("12", "Q")
        card = card.replace("13", "K")
        card = card.replace("14", "A")
        return card
    if card < 10:
        return str(card)
    else:
        return "That's not a card"

def hand_to_string(hand: list) -> str:
    """
    Converts the list into an easily readble string for the player
    """
    if len(hand) == 3:
        return convert_card(hand[0]) + " " + convert_card(hand[1]) + " " + convert_card(hand[2])
    else:
        return "Your hand had doesn't have 3 cards"
    
def sort_hand(hand: list[int]) -> list[int]:
    """
    Sorts from highest to lowest
    
    Listen, I know the code is disgusting, but it works, and it works good, so let it be
    """
    new_hand = hand.copy()
    if len(hand) > 3:
        return [0, 0, 0]
    elif hand[1] > hand[0]:
        new_hand[0] = hand[1]
        new_hand[1] = hand[0]
        if new_hand[2] > new_hand[1]:
            new_hand[1] = hand[2]
            new_hand[2] = hand[0]
            if new_hand[1] > new_hand[0]:
                new_hand[0] = hand[2]
                new_hand[1] = hand[1]
    elif hand[2] > hand[0]:
        new_hand[0] = hand[2]
        new_hand[1] = hand[0]
        new_hand[2] = hand[1]
    elif hand[2] > hand[1]:
        new_hand[2] = hand[1]
        new_hand[1] = hand[2]
    return new_hand

def has_triple(hand: list[int]) -> bool:
    """
    Checks for three of a kind
    """
    if hand[0] == hand[1] and hand[0] == hand[2] and len(hand) == 3:
        return True
    else: 
        return False
    
def has_straight(hand: list[int]) -> bool:
    """
    Determines if hand contains a straight
    """
    if hand[0]-1 == hand[1] and hand[1]-1 == hand[2]:
        return True
    else:
        return False
    
def has_pair(hand: list[int]) -> bool:
    """
    Tells if hand contains a pair (STILL RETURNS TRUE IF HAND IS A THREE OF A KIND)
    """
    if hand[0] == hand[1] or hand[1] == hand[2] or hand[0] == hand[2]: #checking if card 1 and card 3 match is redudant since i can assume it's sorted, but i kept it in because redundancy isn't necissaryly that bad of a thing
        return True
    else:
        return False
    
def score_hand(hand: list[int]) -> int:
    """
    Scores the players hand
    """
    if has_triple(hand):
        feature = 16
    elif has_straight(hand):
        feature = 15
    elif has_pair(hand):
        feature = hand[1] #im proud of this logic
    else:
        feature = 0
    return (feature * (16**3)) + (hand[0] * (16**2)) + (hand[1] * (16**1)) + (hand[2] * (16**0))

def dealer_plays(evil_hand: list[int]) -> bool:
    """
    Returns True if hand has a queen high or better
    """
    score = score_hand(evil_hand)
    if (score // (16**3)) >= 1 or ((score // (16**2)) % 16) >= 12:
        return True
    return False

def play_round() -> int:
    hand = deal()
    print("Here is your hand:")
    print(hand_to_string(hand))
    player_choice = get_choice()
    if player_choice == 'p':
        evil_hand = deal()
        print("Here is the dealers hand:")
        print(hand_to_string(evil_hand))
        if not dealer_plays(evil_hand):
            return 10
        if score_hand(hand) > score_hand(evil_hand):
            return 20
        elif score_hand(evil_hand) > score_hand(hand):
            return -20
        return 10
    elif player_choice == 'f':
        return -10
    
def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")