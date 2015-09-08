import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def write(text, color=None):
    if color.lower() == "red":
        print '\033[91m' + text + bcolors.ENDC
    else:
        print text

class Stack:
    def __init__(self, id):
        self.id = id
        self.__cards = []
        
    def addCard(self, card):
        self.__cards.append(card)
        
    def visualize(self):
        print ""
        print "Stack " + str(self.id) + " has a"
        self.__cards[-1].visualize() # Top Card
        print "With " + str(len(self.__cards)-1) + " card(s) under it"


class Player:
    def __init__(self):
        print "Initialized Player"
    
    def takeTurn(self):
        move = raw_input("What is your move")
        return move

class Card:
    def __init__(self, number, suit):
        self.__number = number
        self.__suit = suit
    
    def visualize(self):
        print self.getName() + " of " + self.getSuit()
        
    def getSuit(self):
        if self.__suit == 0:
            return "Spades"
        elif self.__suit == 1:
            return "Hearts"
        elif self.__suit == 2:
            return "Clubs"
        elif self.__suit == 3:
            return "Diamonds"
        else:
            return "Something Went Wrong"
        
    def getName(self):
        if self.__number == 1:
            return "Ace"
        elif self.__number == 11:
            return "Jack"
        elif self.__number == 12:
            return "Queen"
        elif self.__number ==13:
            return "King"
        else: 
            return str(self.__number)

class Deck:
    def __init__(self, shuffle):
        print "Initialized Deck"
        self.__cards = []
        for i in range(1, 14):  #Card Type
            for s in range(4):  #Card Suit
                self.__cards.append(Card(i, s))
        if shuffle:
            self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.__cards)
    
    def deal(self): #Return and remove top card of deck
        card = self.__cards[-1]
        self.__cards.pop()
        return card
        
class GameOfSolitaire:
    def __init__(self):
        self.__player = Player()
        self.__deck = Deck(shuffle=True)
        self.__stacks = [] #Piles of cards
        self.done = False
        
        for i in range(1,8): #[1..7]
            stack = Stack(i)
            for j in range(i):
                stack.addCard(self.__deck.deal())
            self.__stacks.append(stack)
            
        
    def play(self):
        write("------- Playing ------", "red")
        
        while not self.done:
            turn = self.__player.takeTurn()
            #Deal With Turn
            
            self.visualize()
            
            if self.hasWon():
                self.done = True

        
    def visualize(self):
        for stack in self.__stacks:
            stack.visualize()
            
            
    def hasWon(self):
        #Return if Won
        return False
        
playing = True

if playing:
    game = GameOfSolitaire()
    game.play()