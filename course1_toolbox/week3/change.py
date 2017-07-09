# Uses python3


def get_change(m):
    coins = [10, 5, 1]
    nr_coins_change = 0
    value = m
    for coin in coins:
        if not value:
            break
        remainder = value % coin
        nr_coins_change += (value // coin) if remainder == 0 else (value - remainder) // coin
        value = remainder
    return nr_coins_change


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
