from check_word_letter import word_checker

def get_user_input():
    user_input = ''
    list_of_words = []
    while user_input != 'x':
        user_input = input('Write here: ')
        user_input = user_input.lower()
        print('You have written {}' .format(user_input))

        list_of_words.append(user_input)
        if len(list_of_words) > 1:
            last_letter = list_of_words[-2][len(list_of_words[-2])-1: len(list_of_words[-2])]
        else: last_letter = ''

        # word_checker_paramethers = {
       #     'status': status,
       #     'list_of_words': list_of_words,
       # }
        status, list_of_words, last_letter = word_checker(list_of_words, user_input, last_letter)
        if status == 'mistake':
            break
        elif status == 'ok':
            print('Bravo!')

    print(list_of_words)

    exit()