
tungtunggodrelic = {
        "name":"tungtunggodrelic",
        "cost": 10,
        
}
tungtunggodbat = {
        "name":"tungtunggodbat",
        "cost": 10,
        
}

Purchasables = [tungtunggodrelic,tungtunggodbat]


def shop(self, Purchasables,attackpower,aura,health):
    shopask = input("would you like to shop? ").lower()
    if shopask != "no":
        print(Purchasables,attackpower,aura,health,)
        shopbuy = input("what would you like to purchase? ").lower()
        if shopbuy == "tungtunggodrelic" :
            print('bought item!')
            self.health += 50
            self.aura -= 10
            self.attackpower += 5
            
        elif shopbuy == "tungtunggodbat":
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

