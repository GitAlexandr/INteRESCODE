# Викторина
# Игра на выбор правильного варианта ответа,
# вопросы которой читаются из текстового файла
 
import sys, pickle
 
def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл", file_name, ". Работа программы будет завершена.\n", e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file
 
def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
 
def next_block(the_file):
    """Возвращает очередной блок даных из игрового файла"""
    category = next_line(the_file)
    
    question = next_line(the_file)
 
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
 
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
 
    explanation = next_line(the_file)
 
    return category, question, answers, correct, explanation
 
def welcome(title):
    """Приветствует игрока и сообщает ему тему игры."""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")
 
def save_score(score):
    """Сохраняет результат игры"""
    print("Теперь нужно увековечить Ваша достижение!")
    player = input("Введите Ваше имя: ")
    scores_file = open("scores.bin", "wb+")
    record = (player, score)
    scores = []
    try:
        print("Загружаю таблицу результатов.")
        scores = pickle.load(scores_file)
    except EOFError as e:
        print(e)
        print("Таблица результатов пока пуста, но мы это сейчас исправим!")
    scores_file.close()
    scores.append(record)
    print(scores)
    scores_file = open("scores.bin", "wb")
    pickle.dump(scores, scores_file)
    scores_file.close()
    print("Достижение увековечено!")
 
def show_scores():
    """Показывает результаты предыдущих игр."""
    try:
        scores_file = open("scores.bin", "rb")
    except IOError:
        print("Файл с таблицей результатов не найден.")
    else:
        scores = pickle.load(scores_file)
        print(scores)
        scores_file.close()
 
def game():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
 
        # получение ответа
        answer = input("Ваш ответ: ")
 
        # проверка ответа
        if answer == correct:
            print("Да!", end = " ")
            score += 1
        else:
            print("Нет!", end = " ")
        print(explanation)
        print("Счёт:", score, "\n\n")
 
        # переход к следующему вопросу
        category, question, answers, correct, explanation = next_block(trivia_file)
 
    trivia_file.close()
    print("Это был последний вопрос!")
    print("на вашем счету", score)
    save_score(score)
 
def main_menu():
    choice = None
    while choice != "0":
        print(
    """
    Главное меню игры "Викторина"
    0 - Выйти
    1 - Играть
    2 - Показать результаты предыдущих игр
    """)
        choice = input("Ваш выбор: ")
        # выход
        if choice == "0":
            print("До свидания!")
            # приступаем к игре
        elif choice == "1":
            game()
        # показываем результаты предыдущих игр
        elif choice == "2":
            show_scores()
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
 
 
main_menu()
input("\n\nНажмите Enter, чтобы выйти.")