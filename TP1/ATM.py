balance = 2490
money = {
    100: 50,
    50: 20,
    20: 300,
    10: 0,
    5: 200,
    1: 10
}
amount = int(input("Please input your withdraw amount $:"))
if amount <= 0:
    print("Invalid amount!")
elif 0< amount <=2490:
    balance = balance - amount
    print("You have received $",amount)
    for bill in money:
        count = min(amount // bill, money[bill]) # To fine the Money Paper which fit to the amount money 
        if count > 0:
            print(count,"of","$",bill,"bill")
            amount = amount - (bill * count) #To Find the rest of Money
            money[bill] = money[bill] - count #To show the rest fo Bill in ATM bank 
    if amount == 0:
        print("Your Remaining balance: $", balance)
        print("Remaining in this machine:")
        for remain in money:
            print("$", remain, "bill:", money[remain])
    else:
        print("Sorry! ATM does not have enough money!")
else:
        print("Sorry Not enough money in your ban account!")
