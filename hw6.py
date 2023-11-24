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

# 1. Устанавливаем начальные значения left = 0 и right = len(arr) - 1
# 2. Входим в цикл, пока left не превышает right
# 3. Находим середину массива с по формуле mid = (left + right) // 2
# 4. Сравниваем значение элемента в середине массива с target
# 5. Если значение равно target, возвращаем индекс серединного элемента
# 6. Если значение меньше target, обновляем left = mid + 1 (исключаем левую половину массива)
# 7. Если значение больше target, обновляем right = mid - 1 (исключаем правую половину массива)
# 8. Если цикл завершился без нахождения target, возвращаем -1