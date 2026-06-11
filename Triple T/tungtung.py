import ugui
import shop
import enemies

class tung:
    def __init__(self,health,aura,attackpower):
        self.health = health
        self.aura = aura    #currency
        self.attackpower = attackpower
    def beginnings(self):
        return ugui.beninnings()
    def shopi(self,Purchasables,attackpower,aura,health):
        return shop.shop(self,Purchasables,attackpower,aura,health)
    def enemi(self):
        return enemies.enenimy()
    
#enemies.Enemies      
TripleT=tung(100,10,1)
TripleT.beginnings()
TripleT.shopi(shop.Purchasables,TripleT.attackpower,TripleT.aura,TripleT.health)
TripleT.enemi()

    
            
