class tung:
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
            print("game over")

    def __repr__(self):
        """Developer-friendly representation (safe)."""
        # Copy the dict so we don't modify the original
        safe_dict = {
            k: ("***HIDDEN***" if k in {"answer"} else v)
            for k, v in self.__dict__.items()
        }
        return f"{self.__class__.__name__}({safe_dict})"

    def __str__(self):
        """tung-friendly representation (safe)."""
        return f"tung(health={self.health}, aura={self.aura})"


# Example usage
TripleT=tung(100,10,1)
TripleT.beginnings('')
print(TripleT)          # Uses __str__
print(repr(TripleT))    # Uses __repr__
print(TripleT.health,TripleT.attackpower,TripleT.aura) # Still shows everything unless you filter manually