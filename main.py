from random import choice

words_list = ['Автомобиль', 'Кот', 'Работа', 'Линукс', 'Завод', 'Здоровье']     # Банк слов
cyrillic_lower_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')      # Кирилический алфавит
strike_letters = cyrillic_lower_letters[:]

# # while True:
#     print('_________________________________________________________________________________')
#     print('Главное меню:')
    
#     main_menu = {
#         1 : 'Начать игру',
#         2 : '',
#         3 : 'Выйти из игры',
#     }
    
#     for k,v in main_menu.items():
#         print(k,v)
#     user_action = input()

    
#     if Counter_errors == 5:
#         print('Вы ошиблись много раз. Хотите начать заного? Yes / No ')
#         if input() in ['N', 'n', 'No', 'NO'] :
#             print('Конец игры!')
#             print('_________________________________________________________________________________')
#             break


# print('_________________________________________________________________________________')
# print('Главное меню:')

main_menu = {
    1 : 'Начать игру',
    2 : '',
    3 : 'Выйти из игры',
}

for k,v in main_menu.items():
    print(k,v)
    
#user_action = input()      # Выбор пользователя в меню
user_action = '1'

if user_action == '1':  # Если играем/новая игра
    Word_in_game = choice(words_list)       # Рандомное слово из банка слов words_list, которое сейчас в игре
    Secret_word = ['*'] * len(Word_in_game)     # Закрытое слово по длине слова в игре
    Counter_errors = 0      # Счетчик ошибок
    
    print('____________________________________________________________ ')
    print('Загаданное слово: ', *Secret_word)
    
    while True:
        print('____________________________________________________________')
        user_letter = input("Попробуйте угадать букву: ").lower()
        print()
        Check_Secret = Secret_word[:]       # Копирка спрятанного слова, для сверки изменений

        for ind, letter in enumerate(Word_in_game):
            if letter.lower() == user_letter:       # Если угадал в цикле
                Secret_word[ind] = letter
                
        if user_letter.lower() in strike_letters:
            strike_letters[strike_letters.index(user_letter.lower())] = '*'
                    
        if Check_Secret == Secret_word and user_letter not in ''.join(Secret_word).lower():     # Если не угадал
            Counter_errors += 1
            print('Вы ошиблись')
        else:
            print('ВЫ УГАДАЛИ БУКВУ')
        Check_Secret.clear()
        print(f'Ошибки {Counter_errors}/7')                    
        print('Оставшиеся буквы алфавита: ')
        print(*strike_letters)
        print('____________________________________________________________') 
        print(*Secret_word) 

        if Counter_errors == 7:
            break
        elif '*' not in Secret_word:
            print('____________________________________________________________')
            print("Вы отгадали слово! Поздравляем!")
            print('____________________________________________________________')
            break

    print(f'Игра завершена. Было загадано слово {Word_in_game}. Вы ошиблись {Counter_errors} раз.')
    print('____________________________________________________________')
