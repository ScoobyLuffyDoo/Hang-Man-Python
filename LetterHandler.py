# Replaces letters with # to hide the word
def hide_letters(wordLettersDict,ranWord,hiddenword):
    for dict_key in wordLettersDict:
        dict_letter =wordLettersDict[dict_key]     
        if str(dict_letter) in ranWord:
            hiddenword = hiddenword.replace(dict_letter,'#')
    return hiddenword

# Replaces the correct # with the guessed letter if validation passed 
def replace_correct_Letter(letter, hiddenword, dictionary_collection):
    for dict_key in dictionary_collection:
        dict_letter =dictionary_collection[dict_key]  
        if dict_letter.upper() == letter:        
            hiddenword =hiddenword[:dict_key-1] + letter + hiddenword[dict_key:]
    return hiddenword