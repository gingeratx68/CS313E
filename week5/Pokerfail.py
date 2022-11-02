#  File: Poker.py

#  Description: encrypt text/string by rotating a 2d list clockwise, decrypt by rotating the text/string counter clockwise

#  Student Name: Ginger Hudson

#  Student UT EID: gsh628
#partner mehul gupta 
#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/19/22
#date finished 9/19/22

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
    points = []
    player = []
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
    points=0
    type_of_hand=''

    for hand in self.players_hands:
        points, type_of_hand = self.is_royal(hand)
        if points != 0:
            hand_type.append(type_of_hand)
            hand_points.append(points)
        else:
            points, type_of_hand = self.is_straight_flush(hand)
            if points != 0:
              hand_type.append(type_of_hand)
              hand_points.append(points)
            else:
              points, type_of_hand = self.is_four_kind(hand)
              if points != 0:
                hand_type.append(type_of_hand)
                hand_points.append(points)
              else:
                points, type_of_hand = self.is_full_house(hand)
                if points != 0:
                  hand_type.append(type_of_hand)
                  hand_points.append(points)
                else:
                  points, type_of_hand = self.is_flush(hand)
                  if points != 0:
                    hand_type.append(type_of_hand)
                    hand_points.append(points)
                  else:
                    points, type_of_hand = self.is_straight(hand)
                    if points != 0:
                      hand_type.append(type_of_hand)
                      hand_points.append(points)
                    else:
                      points, type_of_hand = self.is_three_kind(hand)
                      if points != 0:
                        hand_type.append(type_of_hand)
                        hand_points.append(points)
                      else:
                        points, type_of_hand = self.is_two_pair(hand)
                        if points != 0:
                          hand_type.append(type_of_hand)
                          hand_points.append(points)
                        else:
                          points, type_of_hand = self.is_one_pair(hand)
                          if points != 0:
                            hand_type.append(type_of_hand)
                            hand_points.append(points)
                          else:
                            points, type_of_hand = self.is_high_card(hand)
                            hand_type.append(type_of_hand)
                            hand_points.append(points)
    print("")                       
    for i in range(len(hand_type)):
      print('Player ' + str(i + 1) + ': ' + hand_type[i])
      # determine winner and print
    
    
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
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

    if (not rank_order):
      return 0, ''

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight Flush'

  #input the hand
  #outputs the ranks that are the same and the number of such cards
  def check_for_number_of_same_rank(self, hand):
    hand_rank_list = []
    number_of_biggest = 0
    for i in range (len(hand)):
      hand_rank_list.append(hand[i].rank)
    for j in range (len(hand)):
      if hand_rank_list.count(hand[j].rank) > number_of_biggest:
        number_of_biggest = hand_rank_list.count(hand[j].rank)
        biggest_rank = j
    return number_of_biggest, biggest_rank

  def is_four_kind (self, hand):
    
    number_of_biggest, biggest_rank = self.check_for_number_of_same_rank(hand)
    if number_of_biggest < 4:
      return 0, ''

    common = hand[biggest_rank].rank
    hand_rank_list = []
    for i in range (len(hand)):
      hand_rank_list.append(hand[i].rank)
    hand_rank_list.remove(common)

    points = 8 * 15 ** 5 + (hand[biggest_rank].rank) * 15 ** 4 + (hand[biggest_rank].rank) * 15 ** 3
    points = points + (hand[biggest_rank].rank) * 15 ** 2 + (hand[biggest_rank].rank) * 15 ** 1
    points = points + (hand_rank_list[0])

    return points, 'Four of a Kind'


  def is_full_house (self, hand):
    number_of_biggest, biggest_rank = self.check_for_number_of_same_rank(hand)
    if number_of_biggest < 3:
      return 0, ''

    common = hand[biggest_rank].rank
    hand_rank_list = []
    for i in range (len(hand)):
      hand_rank_list.append(hand[i].rank)
    hand_rank_list.remove(common)

    number_of_biggest_two = 0
    for j in range (len(hand)):
      if hand_rank_list.count(hand[j].rank) > number_of_biggest_two:
        number_of_biggest_two = hand_rank_list.count(hand[j].rank)
        biggest_rank_two = j
    if number_of_biggest_two < 2:
      return 0, ''

    points = 7 * 15 ** 5 + (hand[biggest_rank].rank) * 15 ** 4 + (hand[biggest_rank].rank) * 15 ** 3
    points = points + (hand[biggest_rank].rank) * 15 ** 2 + (hand[biggest_rank_two].rank) * 15 ** 1
    points = points + (hand[biggest_rank_two].rank)

    return points, 'Two Pair'

  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    
    return points, 'Flush'


  def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

    if (not rank_order):
      return 0, ''

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight'


  def is_three_kind (self, hand):

    number_of_biggest, biggest_rank = self.check_for_number_of_same_rank(hand)
    if number_of_biggest < 3:
      return 0, ''
    
    same_suit = False
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    common = hand[biggest_rank].rank
    hand_rank_list = []
    for i in range (len(hand)):
      hand_rank_list.append(hand[i].rank)
    hand_rank_list.remove(common)

    points = 4 * 15 ** 5 + (hand[biggest_rank].rank) * 15 ** 4 + (hand[biggest_rank].rank) * 15 ** 3
    points = points + (hand[biggest_rank].rank) * 15 ** 2 + (hand_rank_list[0]) * 15 ** 1
    points = points + (hand_rank_list[1])

    return points, 'Three of a Kind'

  def is_two_pair (self, hand):
    number_of_biggest, biggest_rank = self.check_for_number_of_same_rank(hand)
    if number_of_biggest < 2:
      return 0, ''

    common = hand[biggest_rank].rank
    hand_rank_list = []
    for i in range (len(hand)):
      hand_rank_list.append(hand[i].rank)
    hand_rank_list.remove(common)

    number_of_biggest_two = 0
    for j in range (len(hand)):
      if hand_rank_list.count(hand[j].rank) > number_of_biggest_two:
        number_of_biggest_two = hand_rank_list.count(hand[j].rank)
        biggest_rank_two = j
    if number_of_biggest_two < 2:
      return 0, ''

    points = 3 * 15 ** 5 + (hand[biggest_rank].rank) * 15 ** 4 + (hand[biggest_rank].rank) * 15 ** 3
    points = points + (hand[biggest_rank_two].rank) * 15 ** 2 + (hand[biggest_rank_two].rank) * 15 ** 1
    points = points + (hand_rank_list[2])

    return points, 'Two Pair'

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

    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'High Card'

def main():
  # read number of players from stdin

  # create the Poker object
  game = Poker (3)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
