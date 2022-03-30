a = list(map(int, input().split()))
b = list(map(int, input().split()))
new = list()

i = j = 0

while i < len(a) and j < len(b):
    if a[i] > b[j]:
        new.append(b[j])
        j += 1

    else:
        new.append(a[i])
        i += 1

if i < len(a):
    new += a[i:]
if j < len(b):
    new += b[j:]

print(*new)
