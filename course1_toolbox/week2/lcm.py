# Uses python3


def lcm(a, b):
    cd = gcd(a, b)
    return int((a * b) // cd)


def gcd(a, b):
    if b == 0: return a
    return int(gcd(b, a % b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
