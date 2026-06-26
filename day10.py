import random

name = input("What is your name? ")
print("Good luck!", name)

words = [
    'rainbow', 'computer', 'science', 'programming',
    'python', 'mathematics', 'player', 'condition',
    'reverse', 'water', 'board', 'geeks'
]

word = random.choice(words)

print("\nGuess the characters")

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print("_", end='')
            failed += 1

    if failed == 0:
        print("\nYou Win")
        print("The word is:", word)
        break

    guess = input("\nGuess a character: ").lower()

    if len(guess) != 1:
        print("Please enter a single character")
        continue

    if guess in guesses:
        print("You already guessed that character.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, "more guesses")

    if turns == 0:
        print("You Lose")
        print("The word was:", word)