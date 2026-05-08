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
    TripleT=tung(100,10,0,1)
    TripleT.beginnings("")
def shop(Purchasables):
    shopask = input("would you like to shop?")
    shopask = shopask.lower

    if shopask != "no":
        print(Purchasables,attackpower,aura,health,TripleT)
        shopbuy = input("what would you like to purchase").lower()
        if shopbuy == "tungtunggodrelic" :
            self.health += 50
            
        

            

            shop(Purchasables) 
    