import tungtung
import enemies
from enemies import enemyencounter
def battle():  
    enemy = enemyencounter()
    if enemy is not None and tungtung.TripleT.health > 0:
        if enemy == enemies.eviltungtung:
            print("eviltungtung looks at you with sinister intent")
        if enemy == enemies.evilrabiesdog:
            print("evilrabiesdog drools")
        if enemy == enemies.mutatedsupertung:
            print("mutatedsupertung flexes his arms")
    playerhealth = tungtung.TripleT.health
    playerdamage = tungtung.TripleT.attackpower
    enemyhealth = enemy.enemhealth
    enemyattack = enemy.enemattack
    while tungtung.TripleT.health > 0 and enemy.enemhealth > 0:
        print("you are now in battle!")
        print(f"your health is{playerhealth}and enemies health is{enemyhealth}")
   
        action = input("what action would you like to do? (attack,defend)")
        action = action.lower


        if action == "attack":
            enemyhealth - playerdamage
        print(enemyhealth)
        if action == "defend":
            playerhealth -= enemyattack - 5
        if enemyhealth <= 0:
            tungtung.TripleT.aura += enemy.lootedaura
            print("you win!")    
            break        
