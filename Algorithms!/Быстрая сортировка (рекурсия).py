def quick_sort(s):
    if len(s) <= 1:
        return s

    one = s[0]
    left = [i for i in s if i < one]
    center = [i for i in s if one == i]
    right = list(filter(lambda x: x > one, s))

    return quick_sort(left) + center + quick_sort(right)


print(quick_sort(list(map(int, '16 19 2 12 20 15 20 15'.split()))))
