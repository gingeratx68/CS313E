#  File: Geometry.py

#  Description: OOP with geometrical 3d shapes 

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628

#  Partner Name: Mehul Gupta

#  Partner UT EID: mdg3739

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/16/22

#  Date Last Modified: 9/18/22
import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []	# create a list to store points for hand


    # determine winner and print
    winner=0
    winner_points=0
    hand_type_functions = [self.is_royal, self.is_straight_flush, self.is_four_kind, self.is_full_house, self.is_flush, self.is_straight, self.is_three_kind, self.is_two_pair, self.is_one_pair, self.is_high_card]
    hand_names = ["Royal Flush","Straight Flush","Four of a Kind","Full House","Flush","Straight","Three of a Kind","Two Pair","One Pair","High Card"]
    for hand in self.players_hands:
      for i in len(hand_names):
        total_points=hand_type_functions[i](hand)
        if total_points!=0:
            hand_points.append(total_points)
            hand_type.append(hand_names[i])
            for player in range(len(self.player_hands)):
                print("Player %s: %s" % player, hand_type[i])
            if total_points>winner_points:
                winner_points=total_points
                winner=hand_points[-1]
        print("Player %s wins" % winner)

   
        

  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  def is_straight_flush (self, hand):
    print(hand)

  def is_four_kind (self, hand):
    pass

  def is_full_house (self, hand):
    pass

  def is_flush (self, hand):
    pass

  def is_straight (self, hand):
    pass

  def is_three_kind (self, hand):
    pass

  def is_two_pair (self, hand):
    pass

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        break
    if (not one_pair):
      return 0, ''

    points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'One Pair'

  def is_high_card (self,hand):
    ...
def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
