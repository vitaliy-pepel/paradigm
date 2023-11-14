import math
from functools import reduce

def pearson_correlation(x, y):
    # Проверяем, что длины массивов x и y совпадают
    assert len(x) == len(y), "Длины массивов должны быть одинаковыми"

    # Находим средние значения массивов x и y
    mean_x = reduce(lambda a, b: a + b, x) / len(x)
    mean_y = reduce(lambda a, b: a + b, y) / len(y)

    # Вычисляем числитель и знаменатель формулы корреляции Пирсона
    numerator = reduce(lambda a, b: a + (b[0] - mean_x) * (b[1] - mean_y), zip(x, y), 0)
    denominator = math.sqrt(reduce(lambda a, b: a + (b - mean_x) ** 2, x, 0)) * math.sqrt(reduce(lambda a, b: a + (b - mean_y) ** 2, y, 0))

    # Рассчитываем корреляцию Пирсона
    correlation = numerator / denominator

    return correlation


# Пример использования
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = pearson_correlation(x, y)
print("Корреляция Пирсона:", correlation)