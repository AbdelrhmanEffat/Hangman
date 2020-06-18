import random


def play_game(random_word):
    lives = 8
    hint = '-' * len(random_word)
    won = False
    typed = []

    while lives > 0:
        print()
        print(hint)
        letter = input("Input a letter: ")
            
        if len(letter) != 1:
            print("You should input a single letter")
        elif not letter.islower():
            print("It is not an ASCII lowercase letter")
        elif letter in typed:
            print("You already typed this letter")
        elif letter in random_word:
            for i in range(len(random_word)):
                if letter == random_word[i]:
                    hint = hint[:i] + letter + hint[i+1:]
        else:
            print("No such letter in the word")
            lives -= 1
        
        if hint == random_word:
            won = True
            break
        
        typed.append(letter)

    # display final result
    if won:
        print("You survived!")
    else:
        print("You are hanged!")


# start
print("H A N G M A N")

while True:
    option = input('Type "play" to play the game, "exit" to quit: ')
    
    if option == "play":
        word_list = ['python', 'java', 'kotlin', 'javascript']
        random_word = random.choice(word_list)
        play_game(random_word)
    
    elif option == "exit":
        break
