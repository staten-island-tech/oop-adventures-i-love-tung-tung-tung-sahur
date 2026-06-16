import tungtung
import enemies
from enemies import enemyencounter


def battle():
    enemy = enemyencounter()
    if enemy is None:
        print("no enemy found")
        return


    playerhealth = tungtung.TripleT.health
    playerdamage = tungtung.TripleT.attackpower
    enemyhealth = enemy.enemhealth
    enemyattack = enemy.enemattack


    while playerhealth > 0 and enemyhealth > 0:
        print("you are now in battle!")
        print(f"your health is {playerhealth} and enemies health is {enemyhealth}")
        action = input("what action would you like to do? (attack, defend)").lower()


        if action == "attack":
            enemyhealth -= playerdamage
            playerhealth -= enemyattack
        elif action == "defend":
            playerhealth -= enemyattack - 5
        else:
            print("invalid action u do nothing nerd")
            playerhealth -= enemyattack


        if enemyhealth <= 0:
            tungtung.TripleT.aura += enemy.lootedaura
            print("you win!")
            break
        if playerhealth <= 0:
            print("you died rip")
            break


