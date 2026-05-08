class tung:
    def __init__(self,health,aura,morale,attackpower):
        self.health = health
        self.aura = aura    #currency
        self.morale = morale    #percent increase/decrease multiplier to attackpower
        self.attackpower = attackpower
    def beginnings(self,answer):
        self.answer=answer
        answer = input("wake up?").lower()
        if answer != "no":
            print("welcome big triple t")
        else:
            print("game over")
TripleT=tung(100,10,0,1)
TripleT.beginnings("")


    
        
