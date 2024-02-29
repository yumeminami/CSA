from rich.console import Console

# time complexity: O(n log n)
# space complexity: O(n)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


console = Console()
arr = [64, 34, 25, 12, 22, 11, 90]

console.print(f"[blue]Unsorted array[/blue]: [green]{arr}[/green]")
console.print(f"[blue]Sorted array[/blue]: [green]{quicksort(arr)}[/green]")
