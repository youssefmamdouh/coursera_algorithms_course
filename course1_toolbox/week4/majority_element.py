# Uses python3
import sys

def get_majority_element(a, no_elements):
    counts = {}
    for elem in a:
        counts[elem] = 1 if elem not in counts else counts[elem] + 1
    counts = {v:k for k, v in counts.items()}
    return 1 if max(counts.keys()) > no_elements / 2 else 0

if __name__ == '__main__':
    no_elements = int(input())
    data = list(map(int, input().split()))
    print(get_majority_element(data, no_elements))
