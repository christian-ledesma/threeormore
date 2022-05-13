import random


class Dado:
    def __init__(self):
        pass
    
    def tirar(self):
        return random.randrange(1, 7)
