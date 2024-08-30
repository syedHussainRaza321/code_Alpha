import random

def get_random_word():
    words = ["python", "hangman", "programming", "computer", "algorithm"]
    return random.choice(words)

def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
            
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    guessed_letters = set()
    correct_letters = set()
    tries = 6
    
    print("Let's play Hangman!")
    while tries > 0 and not word_letters.issubset(correct_letters):
        print(display_hangman(tries))
        print("Word: ", " ".join([letter if letter in correct_letters else "_" for letter in word]))
        print("Guessed letters: ", " ".join(guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_letters:
            correct_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {tries} tries left.")
    
    if word_letters.issubset(correct_letters):
        print(f"Congratulations! You've guessed the word '{word}'.")
    else:
        print(display_hangman(tries))
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
