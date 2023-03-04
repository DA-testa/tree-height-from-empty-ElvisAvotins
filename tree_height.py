# python3

import sys
import threading
#import numpy


def compute_height(n, nodes):
    levels = [0] * n
    root = -1
    for i in range(n):
        if nodes[i] == -1:
            root = i
            break
    stack = [root]
    while stack:
        node = stack.pop()
        parent = nodes[node]
        if parent == -1:
            levels[node] = 1
        else:
            levels[node] = levels[parent] + 1
        for i in range(n):
            if nodes[i] == node:
                stack.append(i)

    return max(levels)
def main():
    # implement input form keyboard and from files
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    file_or_input = input()
    size = int(0)
    arr = []
    if file_or_input == "I":
        size = int(input())
        arr = list(map(int, input().split()))
    if file_or_input == "F":
        file_name = (input())
        with open("/home/elvis/RTU/Data_structure/lab2/tree-height-from-empty-ElvisAvotins/test/" + file_name) as f:
            size = int(f.readline())
            arr = list(map(int, f.readline().strip().split()))
    max_depth = compute_height(size, arr)
    print(max_depth)
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
