# python3

import sys
import threading
#import numpy


def compute_height(n, nodes):
    # Write this function
    levels = [0] * n
    for i in range(n):
        parent = nodes[i]
        if parent == -1:
            levels[i] = 1
        else:
            levels[i] = levels[parent] + 1


    return max(levels)
    # Your code here

def main():
    size = int(input())
    arr = list(map(int, input().split()))
    max_depth = compute_height(size, arr)
    print(max_depth)

if __name__ == '__main__':
    main()
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))