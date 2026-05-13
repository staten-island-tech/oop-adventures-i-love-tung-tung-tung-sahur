tungtunggodrelic = {
        "name":"tungtunggodrelic",
        "cost": 10,
        
}
tungtunggodbat = {
        "name":"tungtunggodbat",
        "cost": 10,
        
}

spraythatkillseverything = {
        "name":"spraythatkillseverything",
}
sonion = {
        "name":"sonion",
}














Boss_drops = [spraythatkillseverything,sonion]
Purchasables = [tungtunggodrelic,tungtunggodbat]
class debtmafia:
    def __init__(self,mafiahealth,mafiaattack,debttakenoff):
        self.mafiahealth = mafiahealth
        self.mafiaattack = mafiaattack
        self.debttakenoff = debttakenoff
class boss:
    def __init__(self,bosshealth,bossattack,bosslootedaura):
        self.bosshealth = bosshealth
        self.bossattack = bossattack
        self.bosslootedaura = bosslootedaura

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
    def shop(self, Purchasables,attackpower,aura,health,):
        shopask = input("would you like to shop?").lower()
        if shopask != "no":
            print(Purchasables,attackpower,aura,health,)
            shopbuy = input("what would you like to purchase").lower()
            if shopbuy == "tungtunggodrelic" :
                print('bought item!')
                self.health += 50
                self.aura -= 10
                self.attackpower += 5
                
            if shopbuy == "tungtunggodbat":
                print('bought item!')
                self.aura -= 10
                self.attackpower += 20
            
            else: 
                print("im sorry we dont have that item in stock")
            
            if aura < 0:
                print("you are now in aura debt")
            
            elif aura == 0:
                print("you are now broke")  
    
        


            
        

            

eviltungtung = enemy(40,10,2)
evilrabiesdog = enemy(25,20,3)
mutatedsupertung = enemy(60,10,2)

TripleT=tung(100,10,0,1)
TripleT.beginnings("")
TripleT.shop(Purchasables,TripleT.attackpower,TripleT.aura,TripleT.health)
    