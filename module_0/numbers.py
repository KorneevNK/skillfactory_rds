import numpy as np
from random import randint
count = 0                            # счетчик попыток
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''С каждой попыткой отыскиваем верхнюю и нижнюю границы для генерации случайного числа в этом диапазоне'''
    count = 1 # Первая попытка = 50
    predict = 50 
    low = 1 # Нижняя граница поиска
    high = 101 # Верхняя граница поиска

    while number != predict:
        count += 1
        # Если загаданое число меньше нашей попытки - выше искать бессмысленно. Устанавливаем верхнюю границу
        if predict > number:
        	high = predict 
        # Если загаданное число больше нашей попытки - ниже искать бессмысленно. Устанавливаем нижнюю границу
        else:
        	low = predict + 1 

        # Следующая попытка случайно число между новыми границами
        predict = randint(low,high)
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)