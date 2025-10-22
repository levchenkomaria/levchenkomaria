
#include <iostream>
#include <vector>

// Функция сортировки выбором
void selection_sort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        // Предполагаем, что текущий элемент - минимальный
        int min_index = i;
        // Ищем минимальный элемент в оставшейся части массива
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        // Меняем местами найденный минимальный элемент с текущим
        std::swap(arr[i], arr[min_index]);
    }
}

int main() {
    // Создаем тестовый массив
    std::vector<int> test_array = {64, 25, 12, 22, 11};

    // Выводим исходный массив
    std::cout << "Исходный массив: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Сортируем массив
    selection_sort(test_array);

    // Выводим отсортированный массив
    std::cout << "Отсортированный массив: ";
    for (int num : test_array) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}



#include <iostream>
#include <vector>

using namespace std;

// Функция для слияния двух отсортированных массивов
vector<int> merge(const vector<int>& left, const vector<int>& right) {
    vector<int> result;
    size_t i = 0, j = 0;

    // Пока есть элементы в обоих массивах
    while (i < left.size() && j < right.size()) {
        if (left[i] < right[j]) {
            result.push_back(left[i]);
            i++;
        } else {
            result.push_back(right[j]);
            j++;
        }
    }

    // Добавляем оставшиеся элементы из левого массива
    result.insert(result.end(), left.begin() + i, left.end());
    // Добавляем оставшиеся элементы из правого массива
    result.insert(result.end(), right.begin() + j, right.end());

    return result;
}

// Метод для сортировки массива методом слияния
vector<int> merge_sort(const vector<int>& arr) {
    // Базовый случай: массив длиной 0 или 1 уже отсортирован
    if (arr.size() <= 1) {
        return arr;
    }

    // Находим середину массива
    size_t mid = arr.size() / 2;

    // Делим массив на две части
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());

    // Рекурсивно сортируем каждую часть
    left = merge_sort(left);
    right = merge_sort(right);

    // Сливаем отсортированные части
    return merge(left, right);
}

int main() {
    vector<int> array = {38, 27, 43, 3, 9, 82, 10};
    
    // Выводим исходный массив
    cout << "Исходный массив: ";
    for (int value : array) {
        cout << value << " ";
    }
    cout << endl;

    // Сортируем массив методом слияния
    vector<int> sorted_array = merge_sort(array);

    // Выводим отсортированный массив
    cout << "Отсортированный массив: ";
    for (int value : sorted_array) {
        cout << value << " ";
    }
    cout << endl;

    return 0;
}


#include <iostream>
#include <vector>

void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i; // Инициализируем наибольший элемент как корень
    int left = 2 * i + 1; // левый = 2*i + 1
    int right = 2 * i + 2; // правый = 2*i + 2

    // Проверяем существует ли левый дочерний элемент больший, чем корень
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    // Проверяем существует ли правый дочерний элемент больший, чем текущий наибольший
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    // Меняем корень, если нужно
    if (largest != i) {
        std::swap(arr[i], arr[largest]); // своп

        // Применяем heapify к корню
        heapify(arr, n, largest);
    }
}

void heap_sort(std::vector<int>& arr) {
    int n = arr.size();

    // Построение max-heap
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    // Один за другим извлекаем элементы
    for (int i = n - 1; i > 0; i--) {
        std::swap(arr[0], arr[i]); // меняем корень с последним элементом
        heapify(arr, i, 0);
    }
}

int main() {
    std::vector<int> arr = {12, 11, 13, 5, 6, 7};

    // Выводим исходный массив
    std::cout << "Исходный массив: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Сортируем массив методом heap sort
    heap_sort(arr);

    // Выводим отсортированный массив
    std::cout << "Отсортированный массив: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}

#include <iostream>
#include <vector>

// Функция интерполяционного поиска
int interpolationSearch(const std::vector<int>& arr, int lo, int hi, int x) {
    if (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
        // Вычисляем предполагаемую позицию искомого элемента
        int pos = lo + ((hi - lo) * (x - arr[lo])) / (arr[hi] - arr[lo]);
        // Состояние, если цель найдена
        if (arr[pos] == x)
            return pos;

        // Если x больше, x находится в правом подмассиве
        if (arr[pos] < x)
            return interpolationSearch(arr, pos + 1, hi, x);

        // Если x меньше, x находится в левом подмассиве
        if (arr[pos] > x)
            return interpolationSearch(arr, lo, pos - 1, x);
    }
    return -1;
}

int main() {
    std::vector<int> arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int x = 70; // Искомый элемент

    int result = interpolationSearch(arr, 0, arr.size() - 1, x);

    if (result != -1)
        std::cout << "Элемент найден на позиции: " << result << std::endl;
    else
        std::cout << "Элемент не найден" << std::endl;

    return 0;
}
