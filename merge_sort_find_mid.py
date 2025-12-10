"""
Median Finder using Merge Sort

This program implements a sorting algorithm (merge sort) to sort an array
of numbers and find the median value.

Algorithm: Merge Sort - O(n log n) time complexity
Approach: Divide and conquer - split array, sort halves, merge back

Author:Tianchen Yu
"""


def merge_sort(arr):
    """
    Sort an array using merge sort algorithm.
    
    Merge sort divides the array in half, recursively sorts each half,
    then merges the sorted halves back together.

    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Base case: array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # DIVIDE: find middle point and split into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # CONQUER: recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # COMBINE: merge the two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Compares elements from both arrays one by one, always taking
    the smaller element, until all elements are merged.
    
    
    """
    result = []
    i = 0  # Pointer for left array
    j = 0  # Pointer for right array
    
    # Compare elements from both arrays, take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements from left array
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add any remaining elements from right array
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


def sort_and_find_median(numbers):
    """
    Sort the array and find the median value.
    
    Median is the middle value of a sorted array.
    - For odd-length arrays: middle element
    - For even-length arrays: average of two middle elements
    
    """
    # Handle empty array
    if not numbers:
        raise ValueError("Cannot find median of empty array")
    
    # Sort the array using merge sort
    sorted_numbers = merge_sort(numbers)
    
    # Find median
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        
        mid_right = n // 2
        mid_left = mid_right - 1
        median = (sorted_numbers[mid_left] + sorted_numbers[mid_right]) / 2
    else:
        
        median = sorted_numbers[n // 2]
    
    return median


