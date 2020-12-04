import requests
import random
import json


def get_randomWord():
    url = "https://randomwordgenerator.com/json/words_ws.json"
    response = requests.request("GET",url)
    return_results = response.json()
    randomNumber= random.randint(1,3256)
    randomWord = return_results['data'][randomNumber]["word"]["value"]
    return randomWord
    
def replace_correct_Letter(letter, hiddenword, dictionary_collection):
    for dict_key in dictionary_collection:
        dict_letter =dictionary_collection[dict_key]  
        if dict_letter.upper() == letter:        
            hiddenword =hiddenword[:dict_key-1] + letter + hiddenword[dict_key:]
    return hiddenword

def hide_letters(wordLettersDict,ranWord,hiddenword):
    for dict_key in wordLettersDict:
        dict_letter =wordLettersDict[dict_key]     
        if str(dict_letter) in ranWord:
            hiddenword = hiddenword.replace(dict_letter,'#')
    return hiddenword

input("Press enter to continue")
randomWord = get_randomWord()
word_letters_dict = {}
index = 0
for letters in randomWord:
    index += 1
    word_letters_dict[index] = letters
hiddenword = randomWord
hiddenword =hide_letters(word_letters_dict,randomWord,hiddenword)

print("Random Word has been selected,")
print("Word is : {0}".format(hiddenword))
yes_no = input("Can you Guess the word? Y/N\n")
if yes_no.upper() == "Y":
    GuessWord =""    
    Number_of_Guesses = 6
    while GuessWord.upper() != randomWord.upper() or Number_of_Guesses != 0:
        GuessWord = input("Guess a letter or a word\n")
        GuessWord = GuessWord.upper()
        if GuessWord.upper()  == randomWord.upper():
            break
        elif GuessWord in randomWord.upper():
            hiddenword = replace_correct_Letter(GuessWord,hiddenword,word_letters_dict)
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

    


