#2

def quick_sort(alist, start, end):
    """
    Быстрая сортировка для массива
    :param alist: Изначльный список
    :param start: Позиция старта
    :param end: Позиция конца
    :return: Отсортированный массив
    """
    i = start
    j = end
    arr = alist[(start + end) // 2][1]
    while True:
        while alist[i][1] < arr:
            i += 1
        while alist[j][1] > arr:
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
            j -= 1
        else:
            break
    if start < j:
        quick_sort(alist, start, j)
    if i < end:
        quick_sort(alist, i, end)
