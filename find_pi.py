import math

number = int(input("Enter a positive integer: "))

def find_pi(x):
    pi_str = str(math.pi)

    return pi_str[:(x+1)]

print(find_pi(number))
