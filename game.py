import random

class Card():
	def __init__(self, number, suit):
		self.__number = number
		self.__suit = suit

	def getValue(self):
		return self.__number + (self.__suit/4)

	def draw(self):
		name = str(self.__number) + " of "
		if self.__suit == 0:
			name += "hearts"
		elif self.__suit == 1:
			name += "diamonds"
		elif self.__suit == 2:
			name += "clubs"
		elif self.__suit == 3:
			name += "spades"
		else:
			name += "idk"
		print name

class Deck():
	def __init__(self):
		self.__cards =[]
		for i in range (1, 14):
			for s in range(4):
				self.__cards.append(Card(i, s))
	def shuffle(self):
		random.shuffle(self.__cards)
	
	def deal(self, p1,  p2):
		for i in range(0, len(self.__cards), 2):
			p1.addCardToHand(self.__cards[i])
			p2.addCardToHand(self.__cards[i+1])
	


class Player():
	def __init__(self, id):
		self.__id = id
		self.__hand = []
		self.__points = 0
	def addCardToHand(self, card):
		self.__hand.append(card)

	def incrementPoints(self):
		self.__points += 1

	def getPoints(self):
		return self.__points

	def getTopCard(self):
		return self.__hand[-1]

	def deleteTopCard(self):
		self.__hand.pop()
	
	def putTopCardOn(self, table):
		table.putCardOnTable(self.getTopCard())
		self.deleteTopCard()

	def isOutOfCards(self):
		return len(self.__hand) == 0

class Table():
	def __init__(self):
		self.__cards = []
	
	def getPlayedCards(self):
		return self.__cards

	def display(self):
		for card in self.__cards:
			print(card.draw()),

	def clear(self):
		self.__cards = []

	def putCardOnTable(self, card):
		self.__cards.append(card)

class GameOfWar():
	def __init__(self):
		self.player1 = Player(1)
		self.player2 = Player(2)
		self.table = Table()
		self.deck = Deck()
		self.done = False

	def start(self):
		self.deck.shuffle()

		self.deck.deal(self.player1, self.player2)

		while not self.done:
			self.player1.putTopCardOn(self.table)
			self.player2.putTopCardOn(self.table)

			self.table.display()
			raw_input()

			cards = self.table.getPlayedCards()

			if cards[0].getValue() > cards[1].getValue():
				self.player1.incrementPoints()
				print "Player 1 wins this round!"
			elif cards[1].getValue() > cards[0].getValue():
				self.player2.incrementPoints()
				print "Player 2 wins this round!"
			else:
				print "It's a tie!"

			self.table.clear()

			raw_input()

			if self.player1.isOutOfCards():
				if self.player1.getPoints() > self.player2.getPoints():
					print "Player 1 wins game!"
				elif self.player2.getPoints() > self.player1.getPoints():
					print "Player 2 wins game!"
				else:
					print "Game is a tie"

				self.done = True
if __name__ == "__main__":
	playing = True

	while playing:
		game = GameOfWar()

		game.start()

		playing = raw_input("Continue?  ").lower().startswith("y")

