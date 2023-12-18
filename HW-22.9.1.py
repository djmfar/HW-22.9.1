import random

def insertion_sort(array):
    result = []
    if len(array) == 1:
        result = array
    else:
        middle = len(array) // 2
        array1 = insertion_sort(array[:middle])
        array2 = insertion_sort(array[middle:])
        i, j = 0, 0
        while i < len(array1) and j < len(array2):
            if array1[i] < array2[j]:
                result.append(array1[i])
                i += 1
                if i == len(array1):
                    result.extend(array2[j:])
            else:
                result.append(array2[j])
                j += 1
                if j == len(array2):
                    result.extend(array1[i:])
    return result

def binary_search(array, num):
    left, right = 0, len(array) -1
    middle = len(array) // 2
    if num <= array[left]:
        return 'В последовательности чисел нет числа, меньше заданного.'
    elif num > array[right]:
        return 'В последовательности чисел нет числа, больше или равного заданному.'
    while array[middle] != num and left <= right:
        if num > array[middle]:
            left = middle + 1
        else:
            right = middle - 1
        middle = (right + left) // 2
    while array[middle] == num:
        middle -= 1
    return middle

while True: # ввод последовательности чисел
    array = input('Введите числа через пробел: ').split()
    try:
        array = list(map(float, array)) # попытка преобразования введеных значений в числа
        break
    except:
        print('Это не последовательность чисел!')
while True: # ввод искомого числа
    num = input('Введите число, которое нужно найти: ')
    try:
        num = float(num) # попытка преобразования введенного значения в число
        break
    except:
        print('Это не число!')


array = insertion_sort(array) # сортировка последовательности чисел
print(f'\nОтсортированный список:\n'
      f'array = {array}')
index = binary_search(insertion_sort(array), num)
try: # если задача имеет решение, то оно выводится
    index = int(index)
    print(f'\nИндекс искомого элемента = {index}, т.к.\n'
          f'array[{index}] = {array[index]}   <   {num}\n'
          f'array[{index + 1}] = {array[index + 1]}   =>   {num}')
except: # если решения нет, то выводится соответствующее сообщение
    print(f'\n{index}')

