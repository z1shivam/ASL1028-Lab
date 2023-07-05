class grandfather:
    land = "100 acres"

class father(grandfather):
    gold = "200 kilo"

class son(father):
    name = "Shivam"
    money = "50 crores"

shiv = son()
print(f"{son.name} has land {son.land}, gold {son.gold}, money {son.money}")