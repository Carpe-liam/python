class Pet:
    def __init__(self, name, type, trick, noise):
        self.name = name
        self.type = type
        self.trick = trick
        self.health = 50
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        print(f"Energy: {self.energy} ")
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        print(f"Health: {self.health} ")
        print(f"Energy: {self.energy} ")
        return self

    def play(self):
        self.health += 5
        print(f"Health: {self.health} ")
        return self
        
    def sound(self):
        print(self.noise)
