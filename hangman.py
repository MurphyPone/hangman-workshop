import random

# 1. Greet the player and prompt them to select a difficulty

print("welcome to hangman")
difficulty = input("please select a difficulty: easy, medium, hard\n")

while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Invalid difficulty. Please choose from easy, medium, hard\n")

print(f"selecting a {difficulty} word...")

# 2. open the words.txt file and save all the words to a data structure
all_words = list(set(open("words.txt", "r").read().split()))
filtered_words = []
# 2.1 map "easy" "medium" "hard" to word lengths and guess amounts

if difficulty == "easy":
    turns = 12 
    for word in all_words:
        if len(word) < 5:
            filtered_words.append(word)

if difficulty == "medium":
    turns = 10 
    for word in all_words:
        if len(word) >= 5 and len(word) < 7:
            filtered_words.append(word)

if difficulty == "hard":
    turns = 8
    for word in all_words:
        if len(word) >= 7:
            filtered_words.append(word)

# print(filtered_words)

# 2.2 select a word from the filtered words list

secret_word = random.choice(filtered_words)
#print(secret_word)

# print(secret_word)
guesses = ''


# game loop
while turns > 0:
     
    # counts the number of times a user fails
    failed = 0
     
    # all characters from the input
    # word taking one at a time.
    for char in secret_word: 
         
        # comparing that character with
        # the character in guesses
        if char in guesses: 
            print(char, end=" ")
             
        else: 
            print("_", end=" ")
             
            # for every failure 1 will be
            # incremented in failure
            failed += 1
             
    print()
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win") 
         
        # this print the correct word
        print("The word is: ", secret_word) 
        break
     
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character: ")

    # check input with the character in word, prevent duplicate guessing
    if guess in guesses: 
        print(f"You already guessed '{guess}'")

    elif guess not in secret_word:
        turns -= 1
         
        # if the character doesn’t match the word
        # then “Wrong” will be given as output 
        print("Wrong")
         
        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')
         
        if turns == 0:
            print("The word was: ", secret_word) 
            print("You Lose")

    # every input character will be stored in guesses 
    guesses += guess 

