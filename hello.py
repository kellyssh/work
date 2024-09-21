coffee = 10

while True:
    money = int(input("put your money "))
    if money == 300:
        print("give the coffee.")
        coffee -= 1
    elif money > 300:
        print("give %d won in change" % (money - 300))
        coffee -= 1
    else:
        print("give the money and don't give coffee.")
        print("coffee left is %d." % coffee)
    if coffee == 0:
        print("run out of coffee. stop sale")
        break
