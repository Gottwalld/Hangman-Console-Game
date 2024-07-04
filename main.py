from random import choice

def console_border (output:str) -> None:
    'Обрамляет консольной рамкой вводимую строку'
    print(' *  ' + '-' * len(output) + ' *  ')
    print('| | ' + output + ' | |')
    print(' *  ' + '-' * len(output) + ' *  ')

def words_capitalize(list_new_words:list) -> list:
    'Приводит к capitalize виду слова'
    for i in range(len(list_new_words)):
        list_new_words[i] = list_new_words[i].capitalize()
    return list_new_words

def menu_show(menu:dict) -> None:
    'Показывает в консоли удобное меню'
    print()
    for k,v in menu.items():
        print(k,v)
    print()



#_________________________________________________НАЧАЛО ИГРЫ________________________________________________________________
# Инициализация данных и переменных
main_menu = {
    1 : 'Начать новую игру',
    2 : 'Настройки',
    3 : 'Выйти из игры',
}
    
Hangman = {
    
    1 : '''    
    *----*
        |
        |
        |
        =====''', 
    2 :  '''
    *----*
    O   |
        |
        |
        =====''',
        
    3 :  '''
    *----*
    O   |
   /|\  |
        |
        =====''',
    4 :  '''
    *----*
    O   |
   /|\  |
   /    |
        =====''',
    5 :   '''
    *----*
   [O]  |
   /|\  |
   / \  |
        =====''',
    6 :   '''
    *----*
   [x]  |
   /|\  |
   / \  |
        =====''',   
}

menu_show(main_menu)        # Выводим главное меню
user_action = input()      # Выбор пользователя в меню

# Запуск цикла игры
#_______________________________________________________________________________________________________________________________
while True:
    if user_action == '1':
        Counter_errors, limit = 0, 6      # Счетчик ошибок, Количество возможных ошибок по правилам
        
        cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'      # Кирилический алфавит
        strike_letters = list(cyrillic_lower_letters)
        
        # Блок со списками слов
        words_list = ['Автомобиль', 'Кот', 'Работа', 'Завод', 'Здоровье']     # Банк слов
        new_words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек череп'''.split()
        new_words = words_capitalize(new_words)
        words_list =  words_list + new_words        # Добавляем новые слова для игры
        Word_in_game = choice(words_list)       # Рандомное слово из банка слов words_list, которое сейчас в игре
        Secret_word = ['*'] * len(Word_in_game)     # Закрытое слово по длине слова в игре
        # Конецблока
        
        print('____________________________________________________________ ')
        print('Загаданное слово: ', *Secret_word)
        
        # Цикл отгадывания букв в слове
        while True:
            print('____________________________________________________________')
            user_letter = input("Попробуйте угадать букву: ").lower()
            print()
            Check_Secret = Secret_word[:]       # Копирка спрятанного слова, для сверки изменений

            for ind, letter in enumerate(Word_in_game):
                if letter.lower() == user_letter:       # Если угадал в цикле
                    Secret_word[ind] = letter
                    
            if user_letter.lower() in strike_letters:       # Вычеркиваем буквы из алфавита
                strike_letters[strike_letters.index(user_letter.lower())] = f'-({strike_letters[strike_letters.index(user_letter.lower())]})-'
                        
            if Check_Secret == Secret_word and user_letter not in ''.join(Secret_word).lower():     # Если не угадал вообще
                Counter_errors += 1
                print('Вы ошиблись')
            else:
                print('ВЫ УГАДАЛИ БУКВУ')
            Check_Secret.clear()
            
            if Counter_errors in Hangman:       # Графический вывод виселицы
                print(Hangman[Counter_errors])
            
            if Counter_errors == limit - 1:
                print(f'Еще одна ошибка и он умрет! Ошибки {Counter_errors}/{limit}')
            else: 
                print(f'Ошибки {Counter_errors}/{limit}')
            print('Оставшиеся буквы алфавита: ')
            print(*strike_letters)
            print('____________________________________________________________') 
            print(*Secret_word) 

            if Counter_errors == limit:
                break
            elif '*' not in Secret_word:
                console_border("Вы отгадали слово! Поздравляем!")
                break
            
        console_border(f'Игра завершена. Было загадано слово {Word_in_game}. Вы ошиблись {Counter_errors} раз.')
    elif user_action == '2':
        print('Hello there!')
    elif user_action == '3':
        print('Выход из программы.')
        break
    menu_show(main_menu)
    user_action = input()   