# Import choice from random, so we don't have to type random.choice(), but just choice()
from random import choice

# Create a list of questions baby can ask
questions = ["Why is the sky blue?: ", "Why is there a face on the moon?: ",
             "Where are all the dinosaurs?: "]

# Choose random question from the list
question = choice(questions)
# Ask it and take user answer
answer = input(question).strip().lower()

# Create the loop where baby always ask the same question until user type "just because"
while answer != "just because":
    answer = input("Why?: ").strip().lower()

# When loop is over, show baby response
print("Oh... Okay")
