def get_user_input():
    user_input = ''
    list_of_words = []
    while user_input != 'x':
        user_input = input('Write here: ')
        user_input = user_input.lower()
        print('You have written {}' .format(user_input))
        list_of_words.append(user_input)

        if len(list_of_words) > 1:
            if user_input[0] != first_letter_for_the_next_word:
                print('whoops, you made a mistake!')
                break
            else:
                print('Bravo!')

        first_letter_for_the_next_word = list_of_words[-1][-1]
        print(first_letter_for_the_next_word)


    print(list_of_words)

    exit()