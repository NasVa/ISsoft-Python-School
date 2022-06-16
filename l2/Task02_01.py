def output_nums(n):
    for i in range(1, n+1):
        print(f"{i} - {'even' if i % 2 else 'odd'}")

while True:
    n = int(input("Enter the max integer > 1: "))
    if n > 1:
        break
    else:
        print("Value must be > 1")
output_nums(n)

