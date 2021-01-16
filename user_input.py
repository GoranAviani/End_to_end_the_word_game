def get_user_input():
    user_input = ''
    list_of_words = []
    while user_input != 'x':
        user_input = input('Write here: ')
        user_input = user_input.lower()
        list_of_words.append(user_input)
        

    print(list_of_words)

    exit()