value = 0
while value == 0:
    str_value = input("Enter the number: ")
    if str_value.isdigit():
        value = int(str_value)
numbers_sum = 0
for i in range(2, value):
    if not(value % i): 
        for j in range(2, i):
            if not(i % j):
                break
        else:
            numbers_sum += i
if numbers_sum:
    print("Sum of prime divisors: " + str(numbers_sum))
else:
    print("The entered number has no prime divisors")
        
