import random

##########################
##        Eric          ##
##########################
class Pirate:

    def __init__(self, name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.drinks = 3

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, ninja):
        i = random.randint(0,4)
        if i == 0:
            self.shoot -= ninja.health * 0.35
        elif i == 1:
            self.cutlass -= ninja.health * 0.25
        elif i == 2:
            self.drink += self.health * 0.15
            if self.drinks > 0:
                self.drinks -= 1
        elif i == 3:
            self.peg_leg_breaks -= self.health * 0.2 and self.speed * 0.3
        else:
            return self


#############################
##          Dojo           ##
#############################

# class Pirate:

#     def __init__( self , name ):
#         self.name = name
#         self.strength = 15
#         self.speed = 3
#         self.health = 100

#     def show_stats( self ):
#         print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

#     def attack ( self , ninja ):
#         ninja.health -= self.strength
#         return self
