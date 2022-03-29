# Сортировка слиянием (merge sort)
# https://stepik.org/lesson/372095/step/2?unit=359649

def merge_two_list(a, b):
    c = list()
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    if len(s) == 1:
        return s

    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])

    return merge_two_list(left, right)


print(merge_sort(list(map(int, '6 2 19 5 10 7 11'.split()))))
