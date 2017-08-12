# Uses python3
import random


def partition3(a, l, r):
    x = a[l]
    m1, m2 = l, l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            a[i], a[m1] = a[m1], a[i]
            m2 += 1
        elif a[i] == x:
            m2 += 1
            a[m2], a[i] = a[i], a[m2]
    a[l], a[m1] = a[m1], a[l]
    return m1, m2


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    # print("Pivot: %s (%s)" % (a[k], k))
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    # print("m1, m2: %s, %s" % (m1, m2))
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    no_elements = int(input())
    data = list(map(int,input().split()))
    randomized_quick_sort(data, 0, no_elements - 1)
    for x in data:
        print(x, end=' ')
