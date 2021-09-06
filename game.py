#================+++===============================================#
# Name : Hang Man 
# Description : Hang man game written in python, uses Get request
#               to generate a random word 
# Author : ScoobyLuffyDoo
#==================================================================#

import BuildWord # Gets a Random Word
import LetterHandler # Hide and Show Letters

#====================================#
#=        Game Start                =#
#====================================#
input("Press enter to continue")
randomWord = BuildWord.get_randomWord()
word_letters_dict = {}
index = 0
for letters in randomWord:
    index += 1
    word_letters_dict[index] = letters
hiddenword = randomWord
hiddenword =LetterHandler.hide_letters(word_letters_dict,randomWord,hiddenword)
print("Random word has been Generated,")
print("Word is : {0}".format(hiddenword))
yes_no = input("Can you Guess the word? Y/N\n")
if yes_no.upper() == "Y":
    GuessWord =""    
    Number_of_Guesses = 6
    while Number_of_Guesses > 0:
        # while GuessWord.upper() != randomWord.upper():
        GuessWord = input("Guess a letter or a word\n")
        GuessWord = GuessWord.upper()
        if GuessWord.upper()  == randomWord.upper():
            break
        elif GuessWord in randomWord.upper():
            hiddenword = LetterHandler.replace_correct_Letter(GuessWord,hiddenword,word_letters_dict)
            print("Congratulations the letter {0} is in the word\n".format(GuessWord))
            print("Hint : {0}".format(hiddenword))
        else:
            print("Sorry ! {0}  is not the word or a letter\n".format(GuessWord))
            Number_of_Guesses -=1
            print("You only have {0} guesses left".format(Number_of_Guesses))
    if Number_of_Guesses ==0:
        print("Sorry But you died")       
    elif GuessWord.upper()  == randomWord.upper():
        print("Congratulations You Win the word was {0} is in the word\n".format(randomWord))
else:
     print("Goodbye\n")   

    


