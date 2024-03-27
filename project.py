import random
import time


# Initial Steps to invite in the game:

print("\nWelcome to Hangman game by AASHVI CHAWLA\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!\n\n")
time.sleep(3)
print("YOU HAVE TOTAL 4 LIVES. 🤍🤍🤍🤍\n\n")


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global g
    global a
    global hint
    a=4
    g = []
    words_to_guess = ["wish","obey","tongue","studio","alone","raid","driven","formal","harm","warm","sonic"]
    word = random.choice(words_to_guess)
    hint=word

    if word == "wish":
        print("Hint: To express a desire\n")
    elif word == "obey":
        print("Hint: To follow rules\n")
    elif word == "tongue":
        print("Hint: Speech organ\n")
    elif word == "studio":
        print("Hint: A tiny apartment\n")
    elif word == "alone":
        print("Hint: Completely by yourself\n")
    elif word == "raid":
        print("Hint: Surprise police operation\n")
    elif word == "driven":
        print("Hint: Very motivated\n")
    elif word == "formal":
        print("Hint: Official, ceremonial\n")
    elif word == "harm":
        print("Hint: Damage,injury\n")
    elif word == "warm":
        print("Hint: A moderate heat\n")
    elif word == "sonic":
        print("Hint: Relating to sound\n")
    length = len(word)
    g.append(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    
    
    
# A loop to re-execute the game when the first round ends:
    
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
        hangman()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    global a
    global hint
    limit = 4
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n\n")
        hangman()
    
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n\n")

    else:
        print("\nWRONG GUESS! " +"\n")
        a=a-1
        if a>0:
            print("NUMBER OF LIVES REMAINING:\t")
        for i in range(a):
            print("🤍",sep="",end="")
        print()
        count += 1

        if count == 1:
            
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |\n")
            

        elif count == 2:
            
            print("   _____ \n",
                  "  |     | \n",
                  "  |     |\n",
                  "  |      \n",
                  "  |      \n",
                  "  |      \n",
                  "  |      \n",
                  "  |\n")
            print("Do you want another hint??")
            n=input("For yes, enter'y'. For no, enter'n'\n")
            if n=='n':
                pass
            elif n=='y':
                if hint=="sonic":
                    print("Hint: Ends with c")
                elif hint=="wish":
                    print("Hint: Ends with h")
                elif hint=="obey":
                    print("Hint: Ends with y")
                elif hint=="tongue":
                    print("Hint: Ends with e")
                elif hint=="alone":
                    print("Hint: Ends with e")
                elif hint=="raid":
                    print("Hint: Ends with d")
                elif hint=="driven":
                    print("Hint: Ends with n")
                elif hint=="formal":
                    print("Hint: Ends with l")
                elif hint=="harm":
                    print("Hint: Ends with m")
                elif hint=="warm":
                    print("Hint: Ends with m")
            else:
                print("You entered incorrectly!! We'll take that as a no.")
                pass
            
                   
        elif count == 3:
           
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "  |\n")
           

        elif count == 4:
            print("No Lives Remaining\n\n")
            
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\\ \n"
                  "  |    / \\ \n"
                  "  |\n")
            time.sleep(1)
            print("YOU ARE HANGED!!!\n")
            print("The word was:",g)
            play_loop()

    if word == '_' * length:
        print("CONGRATULATIONS! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

main() 
hangman()
