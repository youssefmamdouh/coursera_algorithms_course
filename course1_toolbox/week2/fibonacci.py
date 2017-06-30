# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    sequence = list()
    sequence.append(0)
    sequence.append(1)
    for index in range(2, n+1):
        sequence.append(sequence[index-1] + sequence[index-2])
    return sequence[n]

n = int(input())
print(calc_fib(n))
