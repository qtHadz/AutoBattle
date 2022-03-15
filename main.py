import random
from tkinter import E

class Deck():
    def __repr__(self):
        return str(self.cards)
    def __init__(self):
        self.cards = ["Empty","Empty","Empty","Empty","Empty"]
    def addCard(self,card,pos):
        self.cards[pos] = card
    def LeftToRight(self):
        return self.cards
    def RightToLeft(self):
        r = self.cards.copy()
        r.reverse()
        return r
    def removePos(self,pos):
        item = self.cards[pos]
        t = []
        for i in range(0,len(self.cards),1):
            if i != pos:
                t.append(self.cards[i])
        self.cards = t
        return item
    def isFull(self):
        for item in self.cards:
            if item == "Empty":
                return False
        return True

class Shop(Deck):
    def __init__(self) -> None:
        super().__init__()
        self.startCoins = 10
    def generateShop(self,size,tier):
        self.cards = []
        for i in range(0,size):
            n = random.randint(0,1)
            if n == 0:
                self.addCard(blank,i)
            else:
                self.addCard(joker,i)
    def rerollShop(self,size,tier):
        self.generateShop(size,tier)
        self.coins -= 1
    def resetCoins(self):
        self.coins = self.startCoins
    def giveCoins(self,amount=1):
        self.coins += amount
    def displayShop(self):
        print(f"{self.LeftToRight()} | Coins={self.coins}")
    def buyItem(self,n):
        if (self.coins >= 3 and playerDeck.isFull()) and len(self.cards) > 0:
            self.coins -= 3
            return self.removePos(n)
        return False


class Card():
    def __init__(self,name,sprite):
        self.name = name
        self.sprite = sprite
        self.damage = 1
        self.health = 1
    def __repr__(self):
        return f"{self.name}: D={self.damage},H={self.health}"

    def takeDamage(self,damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
        self.hurtAbility()
    def attack(self,enemy):
        self.preAttAbility()
        enemy.takeDamage(self.damage)
        self.postAttAbility()
    def die(self,cardList=None,other=None):
        self.deathAbility(cardList,other)
        cardList.remove(self)
        return cardList

    def deathAbility(self,cardList,other):
        return
    def hurtAbility(self):
        return
    def preAttAbility(self):
        return
    def postAttAbility(self):
        return
    def startAbility(self):
        return
    def inFrontDie(self):
        return
    def inFrontAttack(self):
        return

class Joker(Card):
    def __init__(self, name, sprite):
        super().__init__(name, sprite)
        self.damage = 3
        self.health = 1
    def deathAbility(self,cardList,other):
        if other:
            other.health += 1
            other.damage += 3
        return


playerDeck = Deck()
shop = Shop()
blank = Card("Blank","")
joker = Joker("Joker","")


while True:
    shopping = True
    shop.generateShop(3,0)
    shop.resetCoins()
    while shopping:
        print(playerDeck)
        shop.displayShop()
        inp = input("What do you want to do? ")
        if inp.upper() == "E":
            if shop.coins > 0:
                inp = input("You still have coins left, are you sure? (Y|N) ")
                if inp.upper() == "Y":
                    shopping = False
                    break
                else:
                    print("Returned to Shop")
            else:
                shopping = False
                break
        elif inp.upper() == "R":
            shop.rerollShop(3,0)
        else:
            inp = int(inp)
            item = shop.buyItem(inp)
            pos = int(input("Position"))
            if item:
                playerDeck.addCard(item,pos)
            else:
                print("Not Enough Coins or Too Many Cards")
    print(playerDeck.RightToLeft())
    playerDeck.cards[0].die(playerDeck.cards,other=playerDeck.cards[1])
    print(playerDeck.RightToLeft())
    input()







    
