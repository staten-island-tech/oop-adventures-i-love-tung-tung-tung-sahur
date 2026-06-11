import tungtung
import enemies
import random
def encounter():   
    from enemies import enemyencounter
    enemyencounter()
    while enemies.enemyencounter == enemies.eviltungtung and tungtung.TripleT.health > 0 and enemies.eviltungtung.enemhealth > 0:
        fighting == input("what action would you like to do? (attack)")
        fighting = fighting.lower
        if fighting == "attack":
            print("attacked enemy")


encounter()
            

import random
class Character:
   def __init__(self, name, health, attack, defense):
       self.name = name
       self.health = health
       self.attack = attack
       self.defense = defense
   def take_damage(self, damage):
       self.health -= max(0, damage - self.defense)
       return self.health > 0
   def is_alive(self):
       return self.health > 0
def battle(player, enemy):
   print(f"Battle Start: {player.name} vs {enemy.name}")
   while player.is_alive() and enemy.is_alive():
       # Player's turn
       print(f"\n{player.name}'s Turn!")
       damage = random.randint(5, player.attack)
       print(f"{player.name} attacks {enemy.name} for {damage} damage.")
       if not enemy.take_damage(damage):
           print(f"{enemy.name} has been defeated!")
           break
       # Enemy's turn
       print(f"\n{enemy.name}'s Turn!")
       damage = random.randint(5, enemy.attack)
       print(f"{enemy.name} attacks {player.name} for {damage} damage.")
       if not player.take_damage(damage):
           print(f"{player.name} has been defeated!")
           break
   print("\nBattle Over!")
if __name__ == "__main__":
   # Create player and enemy characters
   player = Character(name="Hero", health=100, attack=20, defense=5)
   enemy = Character(name="Goblin", health=80, attack=15, defense=3)
   # Start the battle
   battle(player, enemy)

