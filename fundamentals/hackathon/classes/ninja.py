import random
#############################
##         Tristan         ##
#############################
class Ninja:
    def __init__(self, name):
        self.name = name
        self.strength = 5
        self.shuriken = 10
        self.sneak_attack = 15
        self.speed = 30
        self.health = 100
        self.sushi = 3

    def show_stats(self):
        print(
            f"Name: {self.name}\nShuriken: {self.shuriken}\nStrength: {self.strength}\nSneak_Attack: {self.sneak_attack}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack1(self, pirate):
        i = random.randint(0, 5)
        if i < 4:
            pirate.health -= self.shuriken
        else:
            pirate.health = pirate.health
        self.show_stats()
        return self

    def attack2(self, pirate):
        pirate.health -= self.strength
        self.show_stats()
        return self

    def attack3(self, pirate):
        if self.speed > 5:
            i = random.randint(0, 5)
            if i >3:
                pirate.health -= self.sneak_attack
            else:
                pirate.health = pirate.health
            self.show_stats()
            return self

    def attack4(self):
        if self.sushi > 0:
            self.sushi = self.sushi - 1
            self.health = self.health + 10
            self.speed = self.speed + 10
        else:
            print('OH NO! Out of Sushi!!')
        self.show_stats()
        return self











#############################
##          Dojo           ##
#############################
    #class Ninja:
    # def __init__( self , name ):
    #     self.name = name
    #     self.strength = 10
    #     self.speed = 5
    #     self.health = 100
    
    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    # def attack( self , pirate ):
    #     pirate.health -= self.strength
    #return self