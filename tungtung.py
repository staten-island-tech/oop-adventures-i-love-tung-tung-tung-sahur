tungtunggodrelic = {
        "name":"tungtunggodrelic",
        "cost": 50,
        "addedhealth": 100,
}
tungtunggodbat = {
        "name":"tungtunggodbat",
        "cost": 75,
        "addedattack": 100,
}














Purchasables = [tungtunggodrelic,tungtunggodbat]
class enemy:
    def __init__(self,enemhealth,enemattack,lootedaura):
        self.enemhealth = enemhealth
        self.enemattack = enemattack
        self.lootedaura = lootedaura
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
    def shop(self, Purchasables,attackpower,aura,health):
        shopask = input("would you like to shop?").lower()
        if shopask != "no":
            print(Purchasables,attackpower,aura,health)
            shopbuy = input("what would you like to purchase").lower()
            if shopbuy == "tungtunggodrelic" :
                self.health += 50
            
        

            

    
TripleT=tung(100,10,0,1)
TripleT.beginnings("")
TripleT.shop(Purchasables, TripleT.attackpower, TripleT.aura, TripleT.health)