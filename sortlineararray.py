#Write a program to sort the given array of numbers in ascending order. Return the sorted array. Initial array size will be a maximum of 500 elements.

def sortArray(arr):
    # Write your code here
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

#Create test script covering all scenarios (min 5 test cases)

import unittest
from test import sortArray

class TestSortArray(unittest.TestCase):
    def test_sortArray(self):
        self.assertEqual(sortArray([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(sortArray([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(sortArray([1, 3, 5, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sortArray([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(sortArray([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

#verify the performance of the program for an array of 50000 elements

import time
start_time = time.time()
sortArray([i for i in range(50000)])
print("--- %s seconds ---" % (time.time() - start_time))

#Improve the performance of the program for an array of 50000 elements

def sortArray(arr):
    # Write your code here
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

