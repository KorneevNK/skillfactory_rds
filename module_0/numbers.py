import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")

def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = 50
    while number != predict:
        count+=1
        if number - predict >10:
            predict +=10
        elif predict - number >10:
            predict -=10
        elif number > predict: 
            predict += 2
        elif number < predict: 
            predict -= 3
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)