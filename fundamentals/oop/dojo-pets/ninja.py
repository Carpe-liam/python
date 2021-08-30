import pet
class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.sound()
        #print(self.pet)
    
    def display(self):
        print(f"Hi I'm, {self.first_name} {self.last_name} and this is {self.pet.name} and we love {self.treats} and {self.pet_food}.")


rosko = pet.Pet("Rosko", "dog", "roll over", "Bark")
liam = Ninja("Carpe", "Liam", rosko, "bacon", "kibble")

liam.walk()
liam.feed()
liam.bathe()