class father:
    gold = "5kg"

class son(father):
    money = "50 lakhs"
    name = "Shivam"
    
shivam = son()
print(f"{son.name} has money {son.money} and has gold {son.gold}")
