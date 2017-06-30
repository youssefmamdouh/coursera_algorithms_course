# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if (n <= 1):
        return n

    sequence = list()
    sequence.append(0)
    sequence.append(1)
    for index in range(2, n+1):
        sequence.append((sequence[index-1] + sequence[index-2]) % 10)
    return sequence[n]

if __name__ == '__main__':
    print(get_fibonacci_last_digit_naive(int(input())))
