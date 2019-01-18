string = input("Enter a string: ")

def reverse_string(a_string):
    reversed = ""
    
    for i in range(len(a_string)):
        reversed = a_string[i] + reversed

    return reversed

print(reverse_string(string))


