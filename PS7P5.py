#INPUT PHASE
sum = 0
print("Do you want to do this program?")
answer = input()

#PROCESS AND OUTPUT PHASE
while answer == "Yes":
    print("Please enter the quantity.")
    qty = float(input())
    print("Please enter the price.")
    price = float(input())
    extprice = qty * price
    if extprice > 10000:
        disc = 0.25
    else:
        disc = 0.1
    discount2 = extprice * disc
    total = extprice - discount2
    print("The extended price is:   $" + str(extprice))
    print("The discount amount is:   $" + str(discount2))
    print("The total is:   $" + str(total))
    sum = sum + discount2
    print("Do you want to do this program?")
    answer = input()
print("The sum of all discounts is:  $" + str(sum))