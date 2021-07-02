def count_zeros(arr):
    """
    arr is list of 1s and 0s, with all the 1s first, then the 0s. 
    Return the number of zeros

    >>> count_zeros([1,1,1,1,0,0])
    2

    >>> count_zeros([1,0,0,0,0])
    4

    >>> count_zeros([0,0,0])
    3

    >>> count_zeros([1,1,1,1])
    0
    """
    if arr[0] == 0:
        return len(arr)
    if arr[len(arr)-1] == 1:
        return 0

    lower = 0
    upper = len(arr) - 1
    while upper-lower > 1:
        mid = (lower+upper)//2
        if arr[mid] == 1:
            lower = mid
        if arr[mid] == 0:
            upper = mid
    return len(arr) - upper


def sorted_freq(arr, num):
    """
    given a sorted list arr and number num,
    return number of occurences of num in arr
    >>> sorted_freq([1,1,2,2,2,2,3],2)
    4

    >>> sorted_freq([1,1,2,2,2,2,3],3)
    1

    >>> sorted_freq([1,1,2,2,2,2,3],1)
    2

    >>> sorted_freq([1,1,2,2,2,2,3],4)
    -1
    """

    first_lower = 0
    first_upper = len(arr) - 1
    last_lower = 0
    last_upper = len(arr) - 1

    while first_lower < first_upper or last_lower < last_upper:
        first_mid = (first_lower+first_upper)//2
        last_mid = (last_lower+last_upper+1)//2

        if arr[first_mid] < num:
            first_lower = first_mid + 1
        else:
            first_upper = first_mid

        if arr[last_mid] <= num:
            last_lower = last_mid
        else:
            last_upper = last_mid - 1

    if arr[first_upper] != num:
        return -1
    return last_lower - first_lower + 1


def find_rotated_idx(arr, num):
    """
    finds index of num in arr. arr must be a rotated array of sorted numbers.
    returns index if found, otherwise -1

    >>> find_rotated_idx([3,4,1,2],4)
    1

    >>> find_rotated_idx([6, 7, 8, 9, 1, 2, 3, 4], 8)
    2

    >>> find_rotated_idx([6, 7, 8, 9, 1, 2, 3, 4], 3)
    6

    >>> find_rotated_idx([37,44,66,102,10,22],14)
    -1

    >>> find_rotated_idx([6, 7, 8, 9, 1, 2, 3, 4], 12)
    -1

    """
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid = (left_idx+right_idx)//2

        if arr[mid] == num:
            return mid

        if num >= arr[left_idx]:
            if num < arr[mid]:
                right_idx = mid-1
            else:
                left_idx = mid+1

        elif num <= arr[right_idx]:
            if num < arr[mid]:
                left_idx = mid+1
            else:
                right_idx = mid-1

        else:
            return -1
    return -1


def rotation_count(arr):
    """
    finds number of times sorted array has been rotated CCW
    returns index of lowest number in array

    >>> rotation_count([15, 18, 2, 3, 6, 12])
    2

    >>> rotation_count([7, 9, 11, 12, 5])
    4

    >>> rotation_count([7, 9, 11, 12, 15])
    0
    """
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx < right_idx - 1:
        mid = (left_idx+right_idx)//2

        if arr[mid] < arr[left_idx]:
            right_idx = mid
        elif arr[mid] > arr[right_idx]:
            left_idx = mid
        else:
            return 0

    return right_idx


def find_floor(arr, num):
    """
    find largest element in sorted array arr that is less than or equal to num
    returns that element or -1 if there is no such element

    >>> find_floor([1,2,8,10,10,12,19], 9)
    8

    >>> find_floor([1,2,8,10,10,12,19], 20)
    19

    >>> find_floor([1,2,8,10,10,12,19], 0)
    -1
    """
    left_idx = 0
    right_idx = len(arr) - 1

    if num < arr[0]:
        return -1

    while left_idx < right_idx:
        mid = (left_idx+right_idx+1)//2

        if arr[mid] < num:
            left_idx = mid
        elif arr[mid] > num:
            right_idx = mid-1
        else:
            return num

    return arr[left_idx]
