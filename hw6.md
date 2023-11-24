## Домашнее задание из презентации
```
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

```

## Домашнее задание с семинара
```
# Исправить ошибку и добавить комментарии

import time  # импорт модуля для работы со временем

class Stopwatch:
    def __init__(self):  # конструктор класса
        self.start_time = None  # Время начала работы секундомера
        self.bool_pause_time = False  # Переменная, указывающая, находится ли секундомер в режиме паузы
        self.pause_start_time = None  # Время начала паузы
        self.total_paused_time = 0  # Общее время пауз

    def start(self):  # запускает секундомер или возобновляет его работу после паузы
        if not self.start_time:  # Если секундомер еще не запущен
            self.start_time = time.time()  # Запускаем секундомер
        elif self.bool_pause_time:  # Если секундомер находится в режиме паузы
            self.total_paused_time += time.time() - self.pause_start_time  # Учитываем время паузы
            self.bool_pause_time = False  # Выходим из режима паузы

    def pause(self):  # приостанавливает работу секундомера
        if self.start_time and not self.bool_pause_time:  # Если секундомер запущен и не находится в режиме паузы
            self.bool_pause_time = True  # Входим в режим паузы
            self.pause_start_time = time.time()  # Запоминаем время начала паузы

    def resume(self):  # возобновляет работу секуномера после паузы
        if self.bool_pause_time:  # Если секундомер находится в режиме паузы
            self.bool_pause_time = False  # Выходим из режима паузы
            self.total_paused_time += time.time() - self.pause_start_time  # Учитываем время паузы

    def stop(self):  # останавливает секундомер и сбрасывает все переменные
        self.start_time = None  # Сбрасываем все переменные секундомера
        self.bool_pause_time = False
        self.pause_start_time = None
        self.total_paused_time = 0

    def get_time(self):  # возвращает время работы секундомера в секундах
        if self.start_time:
            if self.bool_pause_time:  # исправленна ошибка
                return self.pause_start_time - self.start_time - self.total_paused_time
            else:
                return time.time() - self.start_time - self.total_paused_time

    def get_time_format(self):  # возвращает время работы секундомера в формате "минуты:секунды"
        times = int(self.get_time()) if self.get_time() is not None else 0
        minutes = times // 60
        sec = times % 60
        return f"{minutes:02}:{sec:02}"


if __name__ == "__main__":  #
    name = Stopwatch()
    # выводятся доступные опции управления, и пользователь выбирает одну из них.

    while True:
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

        choice = input("Choose number: ")
        if choice == "1":
            name.start()
        elif choice == "2":
            name.pause()
        elif choice == "3":
            name.resume()
        elif choice == "4":
            #  выводится общее время работы секундомера и сбрасывается в 0
            total = name.get_time_format()
            print()
            print("time", total)
            name.stop()
        elif choice == "5":
            print("Exit")
            break
        # После каждой оперции выводится общее время работы секундомера
        total = name.get_time_format()
        print()
        print("time", total)
        print()
    # После выхода из цикла выводится общее время работы секундомера
    total = name.get_time_format()
    print("time", total)


import time

a = time.time()
time.sleep(2)
b = time.time()
print(b - a)
```