def swap (arr, idx1, idx2):
    """
    swaps the elements of the array at the identified indices
    """
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

def bubble_sort(arr):
    """
    includes optimization if sort completes early
    okay if data almost sorted; really bad if in reverse order
    """
    for i in range(len(arr)):
        swapped = False
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j-1)
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    """
    selects lowest item in unsorted portion, moves to next position
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap(arr, i, min_idx)
    return arr

def insertion_sort(arr):
    """
    puts the selected element in correct place relative to already-sorted portion
    """
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i - 1, -1, -1):
            if temp < arr[j]:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = temp
                break
            if j == 0:
                arr[0] = temp
    return arr
            
def merge(arr1, arr2):
    """
    merges two sorted arrays
    """
    idx_1 = 0
    idx_2 = 0
    arr = []
    while idx_1 < len(arr1) and idx_2 < len(arr2):
        if arr1[idx_1] < arr2[idx_2]:
            arr.append(arr1[idx_1])
            idx_1 += 1
        else:
            arr.append(arr2[idx_2])
            idx_2 += 1
    if idx_1 < len(arr1):
        arr = arr + arr1[idx_1:len(arr1)]
    else:
        arr = arr + arr2[idx_2:len(arr2)]
    return arr
                
def merge_sort(arr):
    """
    sorts two arrays with merge sort algorithm
    """
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    else:
        arr1 = merge_sort(arr[:len(arr)//2])
        arr2 = merge_sort(arr[len(arr)//2:])
        return merge(arr1, arr2)

def pivot(arr, start = 0, end = 0):
    """
    takes array or portion of an array starting with index start and ending with index end, 
    makes element at the first index the pivot, 
    puts all values less than pivot to left of pivot, and values greater than the pivot to the right
    """
    pvt_idx = start
    if end == 0:
        end = len(arr) - 1
    end_idx = end

    while pvt_idx < end_idx:
        if arr[end_idx] > arr[pvt_idx]:
            end_idx -= 1
        elif arr[pvt_idx] > arr[pvt_idx + 1]:
            swap(arr, pvt_idx, pvt_idx + 1)
            pvt_idx += 1
        else:
            swap(arr, pvt_idx + 1, end_idx)
            end_idx = end_idx - 1
    return pvt_idx

def quick_sort(arr):
    """
    sorts array via quicksort method
    """
    def quick_sort_recursive(arr, start, end):
        if end - start < 1:
            return arr
        else:
            pvt_idx = pivot(arr, start, end)
            quick_sort_recursive(arr, start, pvt_idx - 1)
            quick_sort_recursive(arr, pvt_idx + 1, end)
            return arr

    quick_sort_recursive(arr, 0, len(arr) -1)
    return arr
