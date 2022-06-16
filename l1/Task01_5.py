num1 = 0
num2 = 0
while num1 == num2:
    num1 = 0
    num2 = 0
    print("Enter two different integers > 1")
    while num1 == 0:
        str_num = input("Enter the first number: ")
        if str_num.isdigit() and int(str_num) > 1:
            num1 = int(str_num)
    while num2 == 0:
        str_num = input("Enter the second number: ")
        if str_num.isdigit() and int(str_num) > 1:
            num2 = int(str_num)
for i in range(2, num1 if num1 > num2 else num2):
    if not num1 % i and not num2 % i:
        print(f"{num1} and {num2} are not coprime")
        break
else:
    print(f"{num1} and {num2} are coprime")
