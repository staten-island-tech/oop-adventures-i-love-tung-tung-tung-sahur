class enemy:
        def __init__(self,name,enemhealth,enemattack,lootedaura):
            self.name=name
            self.enemhealth = enemhealth
            self.enemattack = enemattack
            self.lootedaura = lootedaura
# Create a list of Person objects in one line
Enemies = [enemy(name,enemhealth,enemattack,lootedaura) for name,enemhealth,enemattack,lootedaura in [('eviltungtung', 40, 10, 3), ('evilrabiesdog', 25, 20, 3),('mutatedsupertung',60,10,2)]]

for p in Enemies:
    print(p.name,p.enemhealth, p.enemattack,p.lootedaura)