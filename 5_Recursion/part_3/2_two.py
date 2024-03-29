def recursive_bubble_sort(arr, n):
    if n == 1:
        return 
        
    # One pass of bubble sort to move the largest element to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursively sort the remaining elements
    recursive_bubble_sort(arr, n - 1)

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
recursive_bubble_sort(arr, n)

print("Sorted array:", arr)
