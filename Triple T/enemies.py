def enenimy():
    import random

    class enemy:
        def __init__(self,name,enemhealth,enemattack,lootedaura):
            self.name=name
            self.enemhealth = enemhealth
            self.enemattack = enemattack
            self.lootedaura = lootedaura
    m=int()
    eviltungtung = enemy('eviltungtung',40,10,2)
    evilrabiesdog = enemy('evilrabiesdog',25,20,3)
    mutatedsupertung = enemy('mutatedsupertung',60,10,2)
    Enemies = [evilrabiesdog,eviltungtung,mutatedsupertung]
    def enemyencounter():
        enemysearch = input('would you like to search for enemies? ').lower
        if enemysearch != "no":
            print("ok searching for enemies")
            enemyfound = random.choice(Enemies)
            if enemyfound == eviltungtung:
                print("you have encountered a eviltungtung!")
                m=0
            elif enemyfound == evilrabiesdog:
                print("you have found a evilrabiesdog!")
                m=1
            elif enemyfound == mutatedsupertung:
                print("you have found a mutatedsupertung")
                m=2
        else:
            print("too bad")
            if enemyfound == eviltungtung:
                print("you have encountered a eviltungtung!")
                m=0
            elif enemyfound == evilrabiesdog:
                print("you have found a evilrabiesdog!")
                m=1
            elif enemyfound == mutatedsupertung:
                print("you have found a mutatedsupertung")
                m=2
    monster=enemy[m]
    print(monster)


    enemyencounter()
#enenimy()