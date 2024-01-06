from random import randint
class Die():
    def __init__(self):
        self.sides = 20
    def roll_die(self):
        x = randint(1,self.sides)
        print(x)
die_instance = Die()
for i in range(1,10):
    die_instance.roll_die()