def is_palindrome(n):
    is_palindrome() if n[0] == n[len(n)] else n*factorial(n - 1) 

while True:
    n = int(input("Enter the integer > 0: "))
    if n > 1:
        break
    else:
        print("Invalid input")

print(f"{n}! = {factorial(n)}")

