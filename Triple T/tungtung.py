import ugui
import shop
import enemies
#import fight
import random

class tung:
    def __init__(self,health,aura,attackpower):
        self.health = health
        self.aura = aura    #currency
        self.attackpower = attackpower
    def beginnings(self):
        return ugui.beninnings()
    def shopi(self,Purchasables,attackpower,aura,health):
        return shop.shop(self,Purchasables,attackpower,aura,health)
    def enemi(self):
        return enemies.enenimy()
    def take_damage(self, attackpower):
       health -= max(0, attackpower - self.attackpower)
       return self.health > 0
    def is_alive(self):
       return self.health > 0
def battle(player, enemy):
   print(f"Battle Start: {tung.name} vs {enemy.name}")
   while player.is_alive() and enemy.is_alive():
       # Player's turn
       print(f"\n{player.name}'s Turn!")
       damage = random.randint(0, player.attack)
       print(f"{player.name} attacks {enemy.name} for {damage} damage.")
       if not enemy.take_damage(damage):
           print(f"{enemy.name} has been defeated!")
           break
       # Enemy's turn
       print(f"\n{enemy.name}'s Turn!")
       damage = random.randint(0, enemy.attack)
       print(f"{enemy.name} attacks {player.name} for {damage} damage.")
       if not player.take_damage(damage):
           print(f"{player.name} has been defeated!")
           break
   print("\nBattle Over!")  
#enemies.Enemies      
TripleT=tung(100,10,1)
TripleT.beginnings()
TripleT.shopi(shop.Purchasables,TripleT.attackpower,TripleT.aura,TripleT.health)
TripleT.enemi()
battle(TripleT,enemies.Enemies['eviltungtung'])