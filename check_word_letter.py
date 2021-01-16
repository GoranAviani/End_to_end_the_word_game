

def word_checker(list_of_words, user_input, first_letter_for_the_next_word):
    list_of_words.append(user_input)

    if len(list_of_words) > 1:
        print(first_letter_for_the_next_word)

        if user_input[0] != first_letter_for_the_next_word:
            print('whoops, you made a mistake!')
            return 'mistake', list_of_words, ''


    return 'ok', list_of_words, first_letter_for_the_next_word

