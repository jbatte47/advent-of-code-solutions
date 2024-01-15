import random

insults = []

class Housewife:
    num_housewives = 0
    def __init__(self, name, enemy, location, insults, allies):
        self.name = name
        self.enemy = enemy
        self.location = location
        self.insults = insults
        self.allies = allies
        Housewife.num_housewives += 1
        
    @classmethod
    def anticipated_new_housewife(cls, location):
        cls('unknown', '', location, [], [])


    def yell(self):
        insult = random.choice(self.insults)
        return print(insult)
    
    def new_insult(self, insult):
        self.insults.append(insult)
    
    def is_ally(self, ally):
        if ally in self.allies:
            print(f"{ally} is an ally of {self.name}")
        else:
            print(f"{ally} is NOT an ally of {self.name}")


lvp = Housewife("Lisa Vanderpump", "Kyle Richards", "Beverly Hills", ["Life isn't all diamond's and rose", "I love dogs I'm just not crazy about bitches", "Goodbye Kyle!"], ["Brandi", "Adrienne"])

lvp.new_insult("BUT NOW WE SAID IT!")

kyle_richards = Housewife("Kyle Richards", "Lisa Vanderpump", "Beverly Hills", ["Have a piece of bread and maybe you'll calm down a bit!", "Let's talk about the husband"], ["Erika", "Dorit"])

lvp.yell()
kyle_richards.yell()

lvp.is_ally("Brandi")
kyle_richards.is_ally("LVP")

print(Housewife.num_housewives)