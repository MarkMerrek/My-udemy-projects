# Ask user for sentence
original = input("Please enter a sentence: ").strip().lower()

# Split sentence into words
words = original.split()

# Loop through words and convert into pig latin
new_words = []

for word in words:
    # If starts with vowel, just add "yay"
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    # Otherwise, move the first consonant cluster to end, and add "ay"
    else:
        vowel_pos = 0
        # Loop through each letter in the word
        for letter in word:
            # If letter is not a vowel, then go on
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            # If it is a vowel, then just stop looping through
            else:
                break
        # Take a slice of the word up to, but not including that vowel index
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        # Add everything in right order
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# Stick words back together to make a sentence
output = " ".join(new_words)

# Output the final string
print(output)
