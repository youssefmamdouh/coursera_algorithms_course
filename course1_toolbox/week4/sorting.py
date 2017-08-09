# Uses python3
import random

def partition3(a, l, r):
    x = a[l]
    m1, m2 = l, l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            if m1 == m2:
                pass
            else:
                m1 += 1
                m2 += 1
                a[m1], a[i] = a[i], a[m1]
        if a[i] == x:
            pass
    return m1, m2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    print("Pivot: " + str(k))
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    no_elements = int(input())
    data = list(map(int,input().split()))
    randomized_quick_sort(data, 0, no_elements - 1)
    for x in data:
        print(x, end=' ')
