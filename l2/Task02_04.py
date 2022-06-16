def is_palindrome(n):
    if not n // 10:
        return True
    last_digit = n % 10
    first_digit = n
    degree = 0
    while first_digit > 9:
        first_digit //= 10
        degree += 1
    return is_palindrome((n - last_digit - first_digit * (10 ** degree)) // 10) if first_digit == last_digit else False

n = 0
while n < 10:
    n = int(input("Enter the integer > 9: "))
print(f"{n} is{' not' * (not(is_palindrome(n)))} palindrome")

