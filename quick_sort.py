def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


# User input
n = int(input("Enter number of elements: "))

arr = []
print("Enter elements:")

for i in range(n):
    element = int(input())
    arr.append(element)

# Sorting
arr = quick_sort(arr)

print("Sorted array:", arr)
