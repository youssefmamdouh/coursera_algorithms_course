# Uses python3
from functools import reduce


def optimal_points(segments):
    print(segments)
    points = set()
    for index in range(n):
        if index != n-1:
            points.add(min(set(range(segments[index][0], segments[index][1] + 1))
                       .intersection(range(segments[index + 1][0], segments[index + 1][1] + 1))))
    return points


if __name__ == '__main__':
    n = int(input())
    segments = []
    for segment in range(n):
        segments.append(list(map(int, input().split())))
    points = optimal_points(sorted(segments, key=lambda x: x[0], reverse=True))
    print(len(points))
    for p in points:
        print(p, end=' ')
