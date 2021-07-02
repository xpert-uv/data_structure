"""
binary heap class - represented by array
"""

class Heap():
    """
    binary heap class
    parent is at (index - 1)//2
    children at 2*index + 1 and 2*index + 2
    """
    def __init__(self, arr = []):
        self.arr = arr

    def swap(self, idx1, idx2):
        temp = self.arr[idx1]
        self.arr[idx1] = self.arr[idx2]
        self.arr[idx2] = temp

    def add(self, val):
        """
        add given value to heap
        """
        self.arr.append(val)
        current_idx = len(self.arr) - 1
        if current_idx == 0:
            return
        while self.arr[current_idx] > self.arr[(current_idx - 1)//2]:
            self.swap(current_idx, (current_idx - 1)//2)
            current_idx = (current_idx - 1)//2
            if current_idx == 0:
                break

    def remove_max(self):
        """
        remove and return max value in heap
        """
        maximum = self.arr[0]
        last = self.arr.pop()
        self.arr[0] = last
        current_idx = 0
        while 2 * current_idx + 1 < len(self.arr):
            if 2 * current_idx + 2 == len(self.arr) or self.arr[2*current_idx + 1] > self.arr[2*current_idx + 2]:
                max_child_idx = 2 * current_idx + 1
            else:
                max_child_idx = 2 * current_idx + 2

            if self.arr[current_idx] < self.arr[max_child_idx]:
                self.swap(current_idx, max_child_idx)
                current_idx = max_child_idx
            else:
                break

        return maximum


    def __repr__(self):
        return str(self.arr)

arr = [52, 23, 13, 6]
heap = Heap(arr)
print(heap)
heap.add(60)
print(heap)
heap.add(36)
print(heap)
print(heap.remove_max())
print(heap)
heap.add(42)
print(heap)