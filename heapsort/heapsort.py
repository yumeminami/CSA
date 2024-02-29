from rich.console import Console


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

# time complexity: O(n log n)
# space complexity: O(n)


def heapsort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements.
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


console = Console()
arr = [64, 34, 25, 12, 22, 11, 90]

console.print(f"[blue]Unsorted array[/blue]: [green]{arr}[/green]")
console.print(f"[blue]Sorted array[/blue]: [green]{heapsort(arr)}[/green]")
