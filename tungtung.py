

tungtunggodrelic = {
        "name":"tungtunggodrelic",
        "cost": 10,
        'health':50,
        'attack':5
}
tungtunggodbat = {
        "name":"tungtunggodbat",
        "cost": 10,
        'health':0,
        'attack':20
        
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
        self.dmg=attackpower+(attackpower*morale*0.01)
    def damage(self,attackpower,morale):
        self.dmg=attackpower+(attackpower*morale*0.01)
    def beginnings(self,answer):
        self.answer=answer
        answer = input("wake up? ").lower()
        if answer != "no":
            print("welcome big triple t")
        else:
            print("game over")
    def shop(self, Purchasables,attackpower,aura,health,morale):
        shopask = input("would you like to shop? ").lower()
        if shopask != "no":
            print(Purchasables,attackpower,aura,health,)
            shopbuy = input("what would you like to purchase ").lower()
            if aura < 0:
                print("you are now in aura debt")
           
            elif aura == 0:
                print("you are now broke")
            else:
                for item in Purchasables:
                    if shopbuy in Purchasables:
                        print('bought item!')
                        self.aura-=Purchasables[item]['cost']
                        self.health+=Purchasables[item]['health']
                        self.attackpower+=Purchasables[item]['attack']
                    elif shopbuy not in item:
                        print("im sorry we dont have that item in stock")
           
   
       




           
       


           


eviltungtung = enemy(40,10,2)
evilrabiesdog = enemy(25,20,3)
mutatedsupertung = enemy(60,10,2)


TripleT=tung(100,10,0,1)
TripleT.beginnings("")
TripleT.shop(Purchasables,TripleT.attackpower,TripleT.aura,TripleT.health,TripleT.morale)
print('health:',TripleT.health,'aura:',TripleT.aura,'morale:',TripleT.morale,'attackpower:',TripleT.attackpower,'damage:',TripleT.dmg)