

def word_checker(list_of_words, user_input):
    list_of_words.append(user_input)
    if len(list_of_words) > 1:
        last_letter = list_of_words[-2][len(list_of_words[-2]) - 1: len(list_of_words[-2])]
    else:
        last_letter = ''

    if len(list_of_words) > 1:
        if user_input[0] != last_letter:
            print('whoops, you made a mistake!')
            return 'mistake', list_of_words


    return 'ok', list_of_words

