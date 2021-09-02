from classes.ninja import Ninja
from classes.pirate import Pirate
import random

action_list = """
        ~~~~~~~~~~~~ NINJA! CHOOSE YOUR ACTION ~~~~~~~~~~~~~~
        -----------------------------------------------------
        #1 = Throw Shuriken (High damage w/ chance to miss)
        #2 = Kunai Attack!  (Low damage - always hits)
        #3 = Attempt Sneak Attack (Highest Damage ~ if speed is great enough w/ miss chance)
        #4 = Eat Sushi (gain 10 health but - reduce speed -5)
        #5 = quit
Action>> """

class Game:
    def __init__(self):
        print("""
                            WELCOME TO NINJA v PIRATE!
        Here you will face off against the infamous Jack Sparrow, a pirate of some 
        notoriety. Will you defeat him in single combat or will you be another one 
        of his many vanquished foes who've stood in his way of obtaining the ultimate 
                                    treasure?
                    (which is OBVIOUSLY Keira Knightley)
        """)
        self.kakashi = Ninja("Kakashi Hakate")
        self.jack = Pirate("Jack Sparrow")

    def end_game(self):
        print("Thanks for playing!")

    #while loop until health =0
    def run_game(self):
        while self.kakashi.health > 0:
            self.take_action(input(action_list))
            #self.do_action(input(action_list))
        self.end_game(self)



    def take_action(self, act):
    #    if jack.speed < 5:
    #        return
        actions = {
            '1': f'{self.kakashi.name} threw a shuriken at {self.jack.name} for {self.kakashi.shuriken} damage!',
            '2': f'{self.kakashi.name} rushed in and stabbed {self.jack.name} with his kunai for {self.kakashi.strength} damage!',
            '3': f'{self.kakashi.name} attempt to sneak attack {self.jack.name} for {self.kakashi.sneak_attack} damage!',
            '4': f'{self.kakashi.name} ate a sushi for +10 Health! Speed is reduced by -5 and is now at {self.kakashi.speed-5}'
        }
        print(f'\n {actions[act]} \n')
        return self.do_action(act)

    def do_action(self, act):
        if act =='1':
            self.kakashi.attack1(self.jack)
            self.jack.show_stats()
            self.kakashi.show_stats()
        if act =='2':
            self.kakashi.attack2(self.jack)
            self.jack.show_stats()
            self.kakashi.show_stats()
        if act =='3':
            self.kakashi.attack3(self.jack)
            self.jack.show_stats()
            self.kakashi.show_stats()
        if act =='4':
            self.kakashi.health += 10
            self.kakashi.speed -=5
            self.kakashi.show_stats()
        if act == 5:
            self.end_game()

# action_list function which takes input int 
game_1 = Game()
game_1.run_game()




















#kakashi.attack(jack_sparrow)
#jack_sparrow.show_stats()
#   for loop while < actions 

#Use the starter code to make a RPG battle game between ninjas and pirates.
#Customize the attack methods on both the Ninja and Pirate class.
#Have an instance of a ninja and pirate battle it out until one's health is depleted.


"""

black_beard = Pirate("Black Beard")

kakashi.attack(jack_sparrow)
jack_sparrow.show_stats()
black_beard.show_stats()

"""