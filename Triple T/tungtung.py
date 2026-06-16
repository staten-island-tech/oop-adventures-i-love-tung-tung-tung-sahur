tungtunggodrelic = {
        "name":"tungtunggodrelic",
        "cost": 10,
        'health': 50,
        'attack': 5
       
}
tungtunggodbat = {
        "name":"tungtunggodbat",
        "cost": 10,
        'attack': 20
       
}


Purchasables = [tungtunggodrelic,tungtunggodbat]






class tung:
    def __init__(self,health,aura,attackpower):
        self.health = health
        self.aura = aura    #currency
        self.attackpower = attackpower
    def shop(self, Purchasables,attackpower,aura,health):
        shopask = input("would you like to shop?").lower()
        if shopask != "no":
            print(Purchasables,attackpower,aura,health,)
            shopbuy = input("what would you like to purchase").lower()
            if shopbuy == "tungtunggodrelic" :
                print('bought item!')
                self.aura -= Purchasables[0]['cost']
                self.health += Purchasables[0]['health']
                self.attackpower += Purchasables[0]['attack']
               
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
            print(self.__dict__)
    def beginnings(self,answer):
            self.answer=answer
            answer = input("wake up?").lower()
            if answer != "no":
                print("welcome big triple t")
            else:
                ("game over")
           
TripleT=tung(100,10,1)