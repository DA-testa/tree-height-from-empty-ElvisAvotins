# python 3
import os
import sys
import threading
import numpy as np 


def compute_height(n, nodes):
    levels = np.zeros(n, dtype=np.int32)
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

    return np.max(levels)


def main():
    script_dir = os.path.dirname(__file__)
    while True:
        file_or_input = input().strip().lower()
        size = int(0) 
        arr = np.array([], dtype=np.int32)
        if file_or_input == "i":
            size = int(input())
            arr = np.fromstring(input().strip(), sep=' ', dtype=np.int32)
        if file_or_input == "f":
            file_name = input()
            if 'a' in file_name:
                break
            file_path = os.path.join(script_dir, "test", file_name)
            with open(file_path) as f:
                size = int(f.readline())
                arr = np.fromstring(f.readline().strip(), sep=' ', dtype=np.int32)
        max_depth = compute_height(size, arr)
        print(max_depth)
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()