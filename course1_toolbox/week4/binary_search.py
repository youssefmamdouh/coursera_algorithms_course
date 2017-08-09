# Uses python3

def binary_search(a, x):
    left, right = 0, len(a) - 1
    while right >= left:
        guess = (right + left) // 2
        if a[guess] == x:
            return guess
        elif a[guess] > x:
            right = guess - 1
        else:
            left = guess + 1
    return -1

if __name__ == '__main__':
    data = sorted(list(map(int, input().split()[1:])))
    to_search = list(map(int, input().split()[1:]))
    for x in to_search:
        print(binary_search(data, x), end =' ')
