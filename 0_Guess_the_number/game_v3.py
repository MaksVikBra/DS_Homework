import numpy as np

def game_core_v3(number: int = 1) -> int: # функция поиска числа бинарным методом
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # задаем границы поиска
    first = 0 # начальный элемент
    last = 101 # конечныйй элемент
    count = 1 # задаём счётчик попыток (с 1 на случай нахождения загаданного числа копьютером сразу)
    predict_num = np.random.randint(1, 101) # генерация компьютером числа с которого начнем поиск
    
    while number != predict_num: # Зададим условие при котором цикл будет выполняться
        count += 1 
        if predict_num > number: # если сгенерированное компьютером число больше загаданного
            last = predict_num # сдвигаем конечный элемент поиска до сгенерированного компьютером числа
            predict_num = (first + last) // 2 # теперь предполагаемое число это число из середины получившегося списка
        else: # если сгенерированное компьютером число меньше загаданного
            first = predict_num # сдвигаем начальный элемент поиска до сгенерированного компьютером числа
            predict_num = (first + last) // 2 # теперь предполагаемое число это число из середины получившегося списка
    
    return count # возвращаем полученый результат

def score_game(random_predict) -> int: # Функция для оценки
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # здесь будем хранить статистику попыток за 1000 проходов
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число: в среднем за {score} попытки')
    print(f'Ваш алгоритм угадывает число: максимум за {max(count_ls)} попытки')
    print(f'Ваш алгоритм угадывает число: минимум за {min(count_ls)} попытки')

print('Run benchmarking for game_core_v3:')
score_game(game_core_v3)