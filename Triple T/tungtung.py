import ugui
import shop
import enemies
import boss

class tung:
    def __init__(self,health,aura,attackpower):
        self.health = health
        self.aura = aura    #currency
        self.attackpower = attackpower
        
#enemies.Enemies      
TripleT=tung(100,10,1)
TripleT.beginnings()
TripleT.shop(shop.Purchasables,TripleT.attackpower,TripleT.aura,TripleT.health)
TripleT.enemyencounter()

    
            
