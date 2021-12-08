#!/usr/bin/python3
# Kuznik Jakub
# xkuzni04@stud.fit.vutbr.cz

import time
import numpy as np

def main():
    print("hello")

    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(array)



if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
