from functools import reduce


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
ll = list()

for _ in range(n):
    i = int(input())
    ll.append(i)

x = reduce(gcd, ll)
print(x)
