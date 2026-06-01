def enenimy():
    import random

    class enemy:
        def __init__(self,enemhealth,enemattack,lootedaura):
            self.enemhealth = enemhealth
            self.enemattack = enemattack
            self.lootedaura = lootedaura

    eviltungtung = enemy(40,10,2)
    evilrabiesdog = enemy(25,20,3)
    mutatedsupertung = enemy(60,10,2)
    Enemies = [evilrabiesdog,eviltungtung,mutatedsupertung]
    def enemyencounter():
        enemysearch = input('would you like to search for enemies?').lower
        if enemysearch != "no":
            print("ok searching for enemies")
            enemyfound = random.choice(Enemies)
            if enemyfound == eviltungtung:
                print("you have encountered a eviltungtung!")
            elif enemyfound == evilrabiesdog:
                print("you have found a evilrabiesdog!")
            elif enemyfound == mutatedsupertung:
                print("you have found a mutatedsupertung")
        else:
            print("too bad")
            if enemyfound == eviltungtung:
                print("you have encountered a eviltungtung!")
            elif enemyfound == evilrabiesdog:
                print("you have found a evilrabiesdog!")
            elif enemyfound == mutatedsupertung:
                print("you have found a mutatedsupertung")
        


    enemyencounter()