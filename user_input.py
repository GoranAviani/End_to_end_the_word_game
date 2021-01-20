from check_word_letter import word_checker

def get_user_input():
    user_input = ''
    list_of_words = []
    while user_input != 'x':
        user_input = input('Write here: ')
        user_input = user_input.lower()
        print('You have written {}' .format(user_input))



        status, list_of_words = word_checker(list_of_words, user_input)
        if status == 'mistake':
            print('whoops, you made a mistake!')
            break
        elif status == 'ok':
            print('Bravo!')

    print(list_of_words)

    exit()