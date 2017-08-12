#Uses python3


def max_dot_product(a, b):
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    return sum([x*y for (x,y) in zip(a, b)])


if __name__ == '__main__':
    n = int(input())
    a = [int(ai) for ai in input().split()]
    b = [int(bi) for bi in input().split()]
    assert len(a) == len(b) == n
    print(max_dot_product(a, b))
