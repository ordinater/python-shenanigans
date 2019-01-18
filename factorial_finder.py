integer = int(input("Enter a positive integer: "))

def find_factorial(n):
    fact = 1

    for i in range(n):
        fact *= (i + 1)

    return fact

print(find_factorial(integer))
