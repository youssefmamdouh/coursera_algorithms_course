# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

max_1 = max(a)
a.remove(max_1)
max_2 = max(a)
result = max_1 * max_2

print(result)
