# Код содержит больше выражений, чем нужно для задачи;
# но я оставил их для демонстрации синтаксиса.

# Импорт типа (данных) defaultdict из модуля collections
# from collections import defaultdict

# Защита от выполнения на случай импорта
# этого скрипта в каком-то другом скрипте
if __name__ == "__main__":
    # Посмотрим на одну из служебных переменных
    print(f"The __file__ is {__file__}")

    # Открываем файл и сохраняем т.н. "файловый объект"
    # в переменную (это не сам файл, но объект, с помощью
    # которого мы взаимодействуем с открытым файлом)
    # .. — специальное имя, указывающее на родительскую директорию
    with open("../17.txt", "r") as f:
        # Вычитываем все строки из файла
        # (получаем List[str], список строк)
        lines = f.readlines()

        print_limit = 10

        # Знакомый нам range-based for
        for line in lines:
            print_limit -= 1
            if print_limit < 0:
                # Досрочный выход из цикла
                break
            
            # Преобразовываем значение из типа
            # str в тип int
            number = int(line)

            # print(number)
            # if number < 5000:
            #     # Досрочный переход на следующую итерацию
            #     continue

            if number > 5000:
                # Форматная строка; облегчает жизнь, позволяет
                # не конкатенировать строки руками в духе
                # "Number " + str(number) + " is bigger than 5000"
                print(f"Number {number} is bigger than 5000")
            elif number < 5000:  # Вторая ветвь условного оператора
                print(f"Number {number} is less than 5000")
            # elif number < 6000:  # Третья ветвь
            #     pass  # TODO: add some stuff here
            # elif number < 7000:
            #     pass
            else:
                print(f"It's a 5000!")
        
        print("We are done!")

    # По выходу из блока "with .. as .." переменная f
    # не существует, данные освобождены, файл закрыт
    print("The file is closed.")
