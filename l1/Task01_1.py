coins = ""
while len(coins) < 2:
    coins = input("Enter string of coins: ")
count1 = 0
count2 = 0
for i in coins:
    if i in "01":
        if int(i):
            count1 += 1
        else:
            count2 += 1
    else:
        print("Incorrect input")
        break
else:
    if count1 > 0 and count2 > 0:  
        print("Minimum integer number of flips: " + str(count1 if count1 > count2 else count2))
    else:
        print("Entered string consists of the same symbols")
