def is_vowel(letter):
    return letter in 'aeiou'

word = "python"


print("Checking if the last letter of", word, "is a vowel:", is_vowel(word[-1]))
