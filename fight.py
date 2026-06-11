import tungtung
import enemies

def encounter():
    while enemies.enemyfound == enemies.eviltungtung and tungtung.TripleT.health > 0 and enemies.eviltungtung.enemhealth > 0:
        fighting == input("what action would you like to do? (attack)")
        fighting = fighting.lower
        if fighting == "attack":
            print("attacked enemy")


encounter()
            


