x = input("Enter a string: ")
VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def vowel_count(word):
    counter = 0
    for char in word:
        if char in VOWELS: counter +=1

    return counter

print(vowel_count(x))
            
