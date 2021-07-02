import unittest
from sort_functions import bubble_sort, merge, merge_sort, insertion_sort, selection_sort, pivot, quick_sort

class TestSortFunctions(unittest.TestCase):
    def test_bubble_sort(self):
        nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
        nums_sorted = [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
        self.assertEqual(bubble_sort(nums), nums_sorted)
        self.assertEqual(bubble_sort([4, 20, 12, 10, 7, 9]), [4, 7, 9, 10, 12, 20])
        self.assertEqual(bubble_sort([0, -10, 7, 4]), [-10, 0, 4, 7])
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(bubble_sort([]), [])

    def test_merge(self):
        arr1 = [-2,-1,0,4,5,6]
        arr2 = [-3,-2,-1,2,3,5,7,8]
        arr12 = [-3,-2,-2,-1,-1,0,2,3,4,5,5,6,7,8]
        self.assertEqual(merge(arr1, arr2), arr12)
        self.assertEqual(merge([1,3,4,5], [2,4,6,8]), [1,2,3,4,4,5,6,8])
        self.assertEqual(merge([3,4,5], [1,2]), [1,2,3,4,5])
        self.assertEqual(merge([1,2], [3,4,5]), [1,2,3,4,5])

    def test_merge_sort(self):
        nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
        nums_sorted = [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
        self.assertEqual(merge_sort(nums), nums_sorted)
        self.assertEqual(merge_sort([4, 20, 12, 10, 7, 9]), [4, 7, 9, 10, 12, 20])
        self.assertEqual(merge_sort([0, -10, 7, 4]), [-10, 0, 4, 7])
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sort([]), [])

    def test_insertion_sort(self):
        nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
        nums_sorted = [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
        self.assertEqual(insertion_sort(nums), nums_sorted)
        self.assertEqual(insertion_sort([4, 20, 12, 10, 7, 9]), [4, 7, 9, 10, 12, 20])
        self.assertEqual(insertion_sort([0, -10, 7, 4]), [-10, 0, 4, 7])
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(insertion_sort([]), [])

    def test_selection_sort(self):
        nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
        nums_sorted = [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
        self.assertEqual(selection_sort(nums), nums_sorted)
        self.assertEqual(selection_sort([4, 20, 12, 10, 7, 9]), [4, 7, 9, 10, 12, 20])
        self.assertEqual(selection_sort([0, -10, 7, 4]), [-10, 0, 4, 7])
        self.assertEqual(selection_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(selection_sort([]), [])

    def test_pivot(self):
        arr1 = [5, 4, 9, 10, 2, 20, 8, 7, 3]
        arr2 = [8, 4, 2, 5, 0, 10, 11, 12, 13, 16]
        self.assertEqual(pivot(arr1), 3)
        self.assertEqual(pivot(arr2), 4)
        self.assertEqual(set(arr1[:3]), set([2, 3, 4]))
        self.assertEqual(set(arr1[3:]), set([5, 7, 8, 9, 10, 20]))
        self.assertEqual(set(arr2[:4]), set([0, 2, 4, 5]))
        self.assertEqual(set(arr2[4:]), set([8, 10, 11, 12, 13, 16]))

    def test_pivot_args(self):
        arr1 = [5, 4, 9, 10, 2, 20, 8, 7, 3]
        arr2 = [8, 4, 2, 5, 0, 10, 11, 12, 13, 16]
        self.assertEqual(pivot(arr1, 3, 8), 7)
        self.assertEqual(pivot(arr2, 3, 5), 4)
        self.assertEqual(set(arr1[3:7]), set([2, 3, 7, 8]))
        self.assertEqual(set(arr1[7:9]), set([10, 20]))
        self.assertEqual(arr2, [8, 4, 2, 0, 5, 10, 11, 12, 13, 16])

    def test_quick_sort(self):
        nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
        nums_sorted = [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
        self.assertEqual(quick_sort(nums), nums_sorted)
        self.assertEqual(quick_sort([4, 20, 12, 10, 7, 9]), [4, 7, 9, 10, 12, 20])
        self.assertEqual(quick_sort([0, -10, 7, 4]), [-10, 0, 4, 7])
        self.assertEqual(quick_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(quick_sort([]), [])