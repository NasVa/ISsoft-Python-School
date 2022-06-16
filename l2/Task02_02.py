def output_prime_nums(n):
    for i in range(2, n + 1):
        for j in range (2, i):
            if not i % j:
                break
        else:
            print(i)

while True:
    n = int(input("Enter the max integer > 1: "))
    if n > 1:
        break
    else:
        print("Value must be > 1")
output_nums(n)

