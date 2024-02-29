from rich.console import Console


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

console = Console()
console.print(f"[blue]Unsorted array[/blue]: [green]{arr}[/green]")
console.print(f"[blue]Sorted array[/blue]: [green]{bubble_sort(arr)}[/green]")