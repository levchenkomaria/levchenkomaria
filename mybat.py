def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n - 1):
        # Последний элемент на каждой итерации уже на своем месте
        for j in range(n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем местами, если они стоят в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def print_array(arr):
    # Выводим массив
    for num in arr:
        print(num, end=' ')
    print()

if __name__ == "__main__":
    # Создаем исходный массив
    arr = [64, 34, 25, 12, 22, 11, 90]
    # Выводим исходный массив
    print("Исходный массив:")
    print_array(arr)

    # Сортируем массив
    bubble_sort(arr)

    # Выводим отсортированный массив
    print("Отсортированный массив:")
    print_array(arr)


def insertion_sort(array):
    # Проходим по всем элементам массива, начиная со второго
    for i in range(1, len(array)):
        key = array[i]  # Текущий элемент, который нужно вставить
        j = i - 1  # Индекс предыдущего элемента

        # Перемещаем элементы array[0..i-1], которые больше key
        # на одну позицию вперед
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key  # Вставляем key на правильное место

def print_array(array):
    # Выводим массив
    for value in array:
        print(value, end=' ')
    print()

# Основной блок для тестирования
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    print("Исходный массив:")
    print_array(array)

    insertion_sort(array)

    print("Отсортированный массив:")
    print_array(array)



def quick_sort(array, low, high):
    # Основной метод для запуска сортировки
    if low < high:
        # pi - это индекс разбиения, array[pi] находится на своем месте
        pi = partition(array, low, high)

        # Отсортировать элементы до и после разбиения
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def partition(array, low, high):
    # Метод для разбиения массива
    # Выбираем последний элемент в качестве опорного
    pivot = array[high]
    i = low - 1  # Индекс меньшего элемента

    # Проходим по всем элементам, кроме опорного
    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному
        if array[j] <= pivot:
            i += 1
            # Поменять местами array[i] и array[j]
            array[i], array[j] = array[j], array[i]

    # Поменять местами array[i+1] и array[high] (опорный элемент)
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def print_array(array):
    # Вспомогательный метод для вывода массива
    for value in array:
        print(value, end=' ')
    print()

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    print("Исходный массив:")
    print_array(array)

    quick_sort(array, 0, len(array) - 1)

    print("\nОтсортированный массив:")
    print_array(array)


def linear_search(arr, target):
    # Проходим по всем элементам массива
    for i in range(len(arr)):
        # Если нашли искомый элемент
        if arr[i] == target:
            return i  # Возвращаем индекс найденного элемента
    return -1  # Возвращаем -1, если элемент не найден

if __name__ == "__main__":
    # Создаем массив
    array = [3, 5, 2, 7, 9, 1, 4]
    # Вычисляем размер массива (в Python это длина списка)
    size = len(array)

    target = 7  # Искомое значение

    # Вызываем функцию поиска
    result = linear_search(array, target)

    # Выводим результат
    if result != -1:
        print("Элемент найден на позиции:", result)
    else:
        print("Элемент не найден")


. def binary_search(array, target):
    # Метод для выполнения бинарного поиска
    left = 0  # Левая граница поиска
    right = len(array) - 1  # Правая граница поиска

    while left <= right:
        # Находим середину массива
        mid = left + (right - left) // 2

        # Проверяем средний элемент
        if array[mid] == target:
            return mid  # Элемент найден

        # Если искомый элемент меньше среднего
        if array[mid] > target:
            right = mid - 1  # Перемещаемся влево
        else:
            left = mid + 1  # Перемещаемся вправо
    return -1  # Элемент не найден

if __name__ == "__main__":
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7

    result = binary_search(sorted_array, target)

    if result != -1:
        print("Элемент найден на позиции:", result)
    else:
        print("Элемент не найден")



def fibonacci(n):
    if n <= 1:
        return n
    fib = [0] * (n + 2)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Функция поиска Фибоначчи
def fibonacci_search(arr, x):
    n = len(arr)

    # Находим наименьшее число Фибоначчи, большее или равное n
    fib_m2 = 0  # (m-2)'е число Фибоначчи
    fib_m1 = 1  # (m-1)'е число Фибоначчи
    fib_m = fib_m2 + fib_m1

    # Находим m такое, что F[m] >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    # Маркеры для элементов, которые не входят в массив
    offset = -1

    # Поиск с помощью чисел Фибоначчи
    while fib_m > 1:
        # Проверяем возможный индекс
        i = min(offset + fib_m2, n - 1)

        # Если x больше элемента, переходим к правому подмассиву
        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        # Если x меньше элемента, переходим к левому подмассиву
        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        # Элемент найден
        else:
            return i

    # Проверяем последний элемент
    if fib_m1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1  # Элемент не найден

# Основной блок
if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    x = 85

    result = fibonacci_search(arr, x)

    if result != -1:
        print("Элемент найден на позиции:", result)
    else:
        print("Элемент не найден")
