# Uses python3


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
    values = []
    weights = []
    for _ in range(n):
        val, weight = list(map(int, input().split()))
        values.append(val)
        weights.append(weight)
    v_w = zip(values, weights)
    print("{:.10f}".format(get_optimal_value(capacity,
                                             sorted(v_w, key=lambda t: t[0] / t[1],
                                                    reverse=True))))
