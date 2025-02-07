
# -----------------------------------------|
# Poker Hand evaluation system.            |
# -----------------------------------------+


# -----------------------------------------------+
# same_rank                                      |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Return a tally indicative of the number of     |
# times the cards in the hand have the same rank.|
# -----------------------------------------------+

def same_rank(hand):
    tally = 0
    for card in hand:
        test_card_rank = card[0]
        for card in hand:
            if test_card_rank == card[0]:
                tally += 1
    return tally 
    
# -----------------------------------------------+
# royal_flush                                    |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# royal flush and return True or False.          |
# -----------------------------------------------+

def royal_flush(hand):
    suit = hand[0][1]
    tally = 0
    for card in hand:
        if card[0] >= 10 and card[1] == suit:
            tally +=1
    if tally == 5:
        answer = True
    else:
        answer = False
    return answer

# -----------------------------------------------+
# straight_flush                                 |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# straigh flush and return True or False.        |
# -----------------------------------------------+

def straight_flush(hand):
    suit = hand[0][1]
    rank = hand[0][0]
    tally = 0
    for card in hand:
        if card[0] != 14 and card[1] == suit and card[0] == rank:
            tally += 1
        rank += 1
    if tally == 5:
        answer = True
    else:
        answer = False
    return answer

# -----------------------------------------------+
# four_of_a_kind                                 |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# four of a kind and return True or False.       |
# -----------------------------------------------+

def four_of_a_kind(hand):
    tally = same_rank(hand)
    if tally == 17:
        answer = True
    else:
        answer = False
    return answer
    
# -----------------------------------------------+
# full_house                                     |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# full house and return True or False.           |
# -----------------------------------------------+

def full_house(hand):
    tally = same_rank(hand)
    if tally == 13:
        answer = True
    else:
        answer = False
    return answer

# -----------------------------------------------+
# flush                                          |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# flush and return True or False.                |
# -----------------------------------------------+

def flush(hand):
    suit = hand[0][1]
    tally = 0
    for card in hand:
        if card[1] == suit:
            tally += 1
    if tally == 5:
        answer = True
    else:
        answer = False
    return answer
# -----------------------------------------------+
# straight                                       |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# straight and return True or False.             |
# -----------------------------------------------+
    
def straight(hand):
    suit = hand[0][1]
    rank = hand[0][0]
    suit_tally = 0
    rank_tally = 0
    for card in hand:
        if suit == card[1]:
            suit_tally += 1
        if rank == card[0]:
            rank_tally += 1
        rank += 1
    if suit_tally < 5 and rank_tally == 5:
        answer = True
    else:
        answer = False
    return answer

# -----------------------------------------------+
# three_of_a_kind                                |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# three of a kind and return True or False.      |
# -----------------------------------------------+

def three_of_a_kind(hand):
    tally = same_rank(hand)
    if tally == 11:
        answer = True
    else:
        answer = False
    return answer

# -----------------------------------------------+
# two_pair                                       |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# two pair and return True or False.             |
# -----------------------------------------------+

def two_pair(hand):
    tally = same_rank(hand)
    if tally == 9:
        answer = True
    else:
        answer = False
    return answer

# -----------------------------------------------+
# one_pair                                       |
# -----------------------------------------------+
# hand: a 5-card poker hand, represented         |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Test the hand to see if it meets the needs of a|
# one pair and return True or False.             |
# -----------------------------------------------+

def one_pair(hand):
    tally = same_rank(hand)
    if tally == 7:
        answer = True
    else:
        answer = False
    return answer

# -----------------------------------------------+
# Evaluate                                       |
# -----------------------------------------------+
# poker_hand: a 5-card poker hand, represented   |
# as a list of lists, e.g. [[7, 'clubs'], ...]   |
# -----------------------------------------------+
# Return a string, the poker hand evaluation.    |
# Do not change this function.                   |
# -----------------------------------------------+

def evaluate(poker_hand):
    """ Return the string evaluation of a 5-card poker hand """
    
    poker_hand.sort()     # Sort the cards into ascending order
    
    if royal_flush(poker_hand):
        return "Royal Flush"
    elif straight_flush(poker_hand):
        return "Straight Flush"
    elif four_of_a_kind(poker_hand):
        return "Four of a Kind"
    elif full_house(poker_hand):
        return "Full House"
    elif flush(poker_hand):
        return "Flush"
    elif straight(poker_hand):
        return "Straight"
    elif three_of_a_kind(poker_hand):
        return "Three of a Kind"
    elif two_pair(poker_hand):
        return "Two Pair"
    elif one_pair(poker_hand):
        return "One Pair"
    else:
        return "Nothing"
		
# -----------------------------------------------+

def main():
    """ Controls the logic of the poker hand evaluation """
    
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    
    hand1 = [[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]]        # royal flush
    hand2 = [[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]]                 # straight flush
    hand3 = [[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]]             # 4 of a kind
    hand4 = [[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]]             # full house
    hand5 = [[13, "diamonds"], [7, "diamonds"], [2, "diamonds"], [8, "diamonds"], [10, "diamonds"]] # flush 
    hand6 = [[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]]                # straight
    hand7 = [[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]]            # 3 of a kind
    hand8 = [[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]]         # 2 pair
    hand9 = [[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]       # 1 pair
    hand10 =[[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]]        # nothing
    hands = [hand1, hand2, hand3, hand4, hand5, hand6, hand7, hand8, hand9, hand10]
    
    for hand in hands:
        print(hand, "-->", evaluate(hand))

# -----------------------------------------------+

main()
