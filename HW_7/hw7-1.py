class Card:
    def __init__(self, card_str):
        suit_map = {'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades', 'C': 'Clubs'}
        rank_map = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
        self.suit = suit_map[card_str[0]]
        self.rank = rank_map.get(card_str[1], card_str[1])  # Handles numeric ranks directly


def rank_value(rank):
    if rank.isdigit():  # Handles '2' to '10'
        return int(rank)
    ranks = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return ranks.get(rank, 0)

def is_straight(ranks):
    """Check if the hand is a straight."""
    ranks = sorted(ranks)
    # Check normal straight
    if all(ranks[i] + 1 == ranks[i + 1] for i in range(4)):
        return True
    # Check special case: 10, J, Q, K, A
    return ranks == [10, 11, 12, 13, 14]

def evaluate_hand(cards):
    if len(cards) != 5:
        return 0  # Invalid number of cards
    
    suits = [card.suit for card in cards]
    ranks = [rank_value(card.rank) for card in cards]
    suit_set = set(suits)
    rank_set = set(ranks)
    rank_count = {rank: ranks.count(rank) for rank in rank_set}

    # Checking for Straight Flush or Straight
    if is_straight(ranks):
        if len(suit_set) == 1:
            return 9  # Straight Flush
        else:
            return 5  # Straight
    
    # Checking for Four of a Kind or Full House
    if max(rank_count.values()) == 4:
        return 8  # Four of a Kind
    if 3 in rank_count.values() and 2 in rank_count.values():
        return 7  # Full House
    
    # Checking for Flush
    if len(suit_set) == 1:
        return 6  # Flush
    
    # Checking for Three of a Kind, Two Pair, One Pair
    if 3 in rank_count.values():
        return 4  # Three of a Kind
    if list(rank_count.values()).count(2) == 2:
        return 3  # Two Pair
    if 2 in rank_count.values():
        return 2  # One Pair

    # If no other hand, it's a High Card
    return 1  # High Card

input_cards = input().split(',')
cards = [Card(code) for code in input_cards]
print(evaluate_hand(cards))  # Output should be 9 for a Straight Flush
