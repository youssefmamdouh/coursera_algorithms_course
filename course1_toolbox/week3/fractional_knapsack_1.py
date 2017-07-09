# Uses python3
from collections import OrderedDict


def get_optimal_value(capacity, sorted_v_w):
    value = 0.
    available_capacity = capacity
    for (val, weight) in sorted_v_w:
        if available_capacity > 0:
            item_weight = min(available_capacity, weight)
            available_capacity -= item_weight
            value += (item_weight * (val / weight))
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    v_w = zip(values, weights)
    opt_value = get_optimal_value(capacity, sorted(v_w, key=lambda t: t[0] // t[1], reverse=True))
    print("{:.4f}".format(opt_value))
