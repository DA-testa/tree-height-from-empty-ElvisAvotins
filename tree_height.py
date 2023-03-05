# import os
import sys
import threading
import numpy as np


def compute_height(size, nodes):
    levels = np.zeros(size, dtype=int)
    root = np.where(nodes == -1)[0][0]
    stack = np.array([root])
    while len(stack) > 0:
        node = stack[-1]
        parent = nodes[node]
        if parent == -1:
            levels[node] = 1
        else:
            levels[node] = levels[parent] + 1
        children = np.where(nodes == node)[0]
        stack = np.concatenate((stack[:-1], children[::-1]))
    return np.max(levels)


def main(): 
    # script_dir = os.path.dirname(__file__)
    size = 0
    file_or_input = input().strip().lower()
    arr = []
    if file_or_input == "i":
        size = int(input())
        list_numbers = input().strip()
        arr = np.fromstring(list_numbers, dtype=int, sep=' ')
    if file_or_input == "f":
        file_name = input().strip()
        if 'a' in file_name:
            return
        file_path = ("test/" + file_name)
        with open(file_path) as f:
            size = int(f.readline())
            arr = np.fromstring(f.readline().strip(), dtype=int, sep=' ')
    max_depth = compute_height(size, arr)
    print(max_depth)
    # os._exit(0)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
