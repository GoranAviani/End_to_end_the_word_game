

def word_checker(list_of_words, user_input):
    list_of_words.append(user_input)
    if len(list_of_words) > 1:
        last_letter = list_of_words[-2][len(list_of_words[-2]) - 1: len(list_of_words[-2])]
        if user_input[0] != last_letter:
            return 'mistake', list_of_words
    else:
        last_letter = ''

    return 'ok', list_of_words

