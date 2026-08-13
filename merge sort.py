import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# User input
arr = list(map(int, input("Enter elements separated by spaces: ").split()))

print("\nOriginal array:", arr)

# Calculate execution time
start_time = time.perf_counter()

sorted_arr = merge_sort(arr)

end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("Sorted array:", sorted_arr)
print("Execution time:", execution_time, "seconds")

# Time complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")
print("Space        : O(n)")
