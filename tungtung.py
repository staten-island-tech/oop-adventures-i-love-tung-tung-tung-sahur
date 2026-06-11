import enemies


tungtunggodrelic = {
        "name":"tungtunggodrelic",
        "cost": 10,
        
}
tungtunggodbat = {
        "name":"tungtunggodbat",
        "cost": 10,
        
}

Purchasables = [tungtunggodrelic,tungtunggodbat]



class tung:
    def shop(self, Purchasables,attackpower,aura,health):
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
    def __init__(self,health,aura,attackpower):
        self.health = health
        self.aura = aura    #currency
        self.attackpower = attackpower
    def beginnings(self,answer):
            self.answer=answer
            answer = input("wake up?").lower()
            if answer != "no":
                print("welcome big triple t")
            else:
                ("game over")

        


            
        
            
TripleT=tung(100,10,1)
TripleT.beginnings("")
TripleT.shop(Purchasables,TripleT.attackpower,TripleT.aura,TripleT.health)
TripleT.enemies()
    

    
            
