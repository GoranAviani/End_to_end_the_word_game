from check_word_letter import word_checker

def get_user_input():
    user_input = ''
    list_of_words = []
    while user_input != 'x':
        user_input = input('Write here: ')
        user_input = user_input.lower()
        print('You have written {}' .format(user_input))

        if len(list_of_words) > 0:
            first_letter_for_the_next_word = list_of_words[-1][-1]
        else:
            first_letter_for_the_next_word = ''

        # word_checker_paramethers = {
       #     'status': status,
       #     'list_of_words': list_of_words,
       # }
        status, list_of_words, first_letter_for_the_next_word = word_checker(list_of_words, user_input, first_letter_for_the_next_word)
        if status == 'mistake':
            break
        elif status == 'ok':
            print('Bravo!')

    print(list_of_words)

    exit()