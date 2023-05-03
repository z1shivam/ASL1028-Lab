#wap to determine profit or loss

cp = float(input("enter the cost price: "))
sp = float(input("enter the selling price: "))

if sp>cp:
    profit = sp - cp
    print("the seller has made the profit of Rs", profit)
if cp > sp:
    loss = cp - sp
    print("the seller has made the loss of Rs", loss)

