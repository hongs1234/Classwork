letter = input("Enter a letter from the alphabet: ")
vowels = {"a", "e", "i", "o", "u"}


if letter in vowels:
    print("This is a vowel")
elif letter == "y":
    print("Sometimes a vowel, sometimes a consonant")
else:
    print("This is a consonant")