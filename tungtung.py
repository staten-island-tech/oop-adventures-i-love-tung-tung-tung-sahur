class tung:
    def __init__(self,health,aura,morale,attackpower):
        self.health = health
        self.aura = aura
        self.morale = morale
        self.attackpower = attackpower
    def beginnings():
        answer = input("wake up?")
        answer = answer.lower
        if answer == "yes":
            print("welcome big triple t")
        
        elif answer == "no":
            print("game over")
        return

    beginnings()


    
        
