class father:
    land = "1000 acres"

class mother:
    gold = "300 killo"

class son(father, mother):
    name = "shivam"
    money = "1000 crores"

shiv = son()
print(f"{son.name} has land {son.land}, gold {son.gold} and money {son.money}")