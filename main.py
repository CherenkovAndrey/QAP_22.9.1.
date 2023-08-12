def insertion_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    return array
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    position = -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < target:
            position = mid
            low = mid + 1
        else:
            high = mid - 1
    return position

input_sequence = input("Введите последовательность чисел через пробел: ")
target_number = input("Введите число для поиска: ")

try:
    sequence = list(map(int, input_sequence.split()))
    target = int(target_number)
    sorted_sequence = insertion_sort(sequence)
    index = binary_search(sorted_sequence, target)

    if index < 0:
        print("Число меньше всех элементов в последовательности")
    elif index >= len(sorted_sequence) - 1:
        print("Число больше всех элементов в последовательности")
    else:
        print("Отсортированный список чисел:", sorted_sequence)
        print("Ближайшее число к",target,"которое меньше введенного числа, а следующее за ним больше или равно ->",sorted_sequence[index],"находится на позиции",index+1)
except ValueError:
    print("Ошибка: некорректный ввод чисел")