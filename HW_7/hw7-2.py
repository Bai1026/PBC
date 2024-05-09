class Card:
    def __init__(self, card_str):
        suit_map = {'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades', 'C': 'Clubs'}
        rank_map = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
        self.suit = suit_map[card_str[0]]
        self.rank = rank_map.get(card_str[1:], card_str[1:])  # Handles numeric and face card ranks properly

class Deck:
    def __init__(self, cards_str):
        self.cards = [Card(card.strip()) for card in cards_str.split(',')]

    def evaluate_hand(self):
        return evaluate_hand(self.cards)

def evaluate_hand(cards):
    suits = [card.suit for card in cards]
    ranks = [rank_value(card.rank) for card in cards]
    suit_set = set(suits)
    rank_set = set(ranks)
    rank_count = {rank: ranks.count(rank) for rank in rank_set}

    # Check for various poker hands
    if is_straight(ranks):
        if len(suit_set) == 1:
            return 9  # Straight Flush
        else:
            return 5  # Straight
    if max(rank_count.values()) == 4:
        return 8  # Four of a Kind
    if 3 in rank_count.values() and 2 in rank_count.values():
        return 7  # Full House
    if len(suit_set) == 1:
        return 6  # Flush
    if 3 in rank_count.values():
        return 4  # Three of a Kind
    if list(rank_count.values()).count(2) == 2:
        return 3  # Two Pair
    if 2 in rank_count.values():
        return 2  # One Pair
    return 1  # High Card

def rank_value(rank):
    ranks = {'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'T': 10}
    return int(ranks.get(rank, rank))  # Directly return the integer of ranks

def is_straight(ranks):
    ranks = sorted(ranks)
    if ranks == [2, 3, 4, 5, 14]:  # Special case for Ace to Five
        return True
    return all(ranks[i] + 1 == ranks[i + 1] for i in range(4))

def process_input(input_data):
    parts = input_data.strip().split('\n')
    num_players = int(parts[0].strip())
    players = []
    card_lines = parts[1:num_players+1]
    names = parts[num_players + 1].strip().split(',')

    if len(names) != num_players:
        raise ValueError("Mismatch between number of players and names provided.")

    for i in range(num_players):
        cards_str = card_lines[i].strip()
        name = names[i].strip()
        deck = Deck(cards_str)
        players.append((name, deck))

    return players

def find_winners(players):
    results = [(name, deck.evaluate_hand()) for name, deck in players]
    max_score = max(score for _, score in results)
    winners = [name for name, score in results if score == max_score]
    if len(winners) == 1:
        return winners[0]
    else:
        return len(winners)


input_str = ""
num = input()
input_str += num
for _ in range(int(num)):
    input_str += '\n'
    input_str += input()

input_str += '\n'
input_str += input()

players = process_input(input_str)
winners = find_winners(players)
print(winners)
