import random
def choose_word():
    # List of words for the game
    words = ['apple', 'banana', 'cherry', 'orange', 'pear', 'strawberry', 'mango','watch','cup','nail','pillow','bed','scarf','car','bike','laptop','flower','book','window','furniture','fortune','mobile','sanitizer','python','java','joke','charger','keyboard','google','emotion']
    return random.choice(words)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    tries = 10
    
    while tries > 0:
        # Display current progress
        display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(f'Word: {display_word}')
        print(f'Tries left: {tries}')
        
        # Ask for user input
        guess = input('Guess a letter: ').lower()
        
        if guess in guessed_letters:
            print(f'You already guessed "{guess}". Try another letter.')
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f'Good guess! "{guess}" is in the word.')
        else:
            print(f'Oops! "{guess}" is not in the word.')
            tries -= 1
        
        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in word):
            print(f'Congratulations! You guessed the word "{word}" correctly.')
            break
    
    if tries == 0:
        print(f'Sorry, you ran out of tries. The word was "{word}".')

# Main function to start the game
if __name__ == "__main__":
    print("Welcome to Hangman!")
    play_hangman()