# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(input())
        self.parent = list(map(int, input().split()))

    def compute_height(self):
        maxHeight = 0
        heights_dict = {node:0 for node in range(self.n)}
        for vertex in range(self.n):
            if (vertex in heights_dict and heights_dict[vertex] != 0):
                continue
            node = vertex
            while node != -1:
                if (node in heights_dict and heights_dict[node] != 0):
                    heights_dict[vertex] += heights_dict[node]
                    break
                heights_dict[vertex] += 1
                node = self.parent[node]
            maxHeight = max(maxHeight, heights_dict[vertex])
        return maxHeight



def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
