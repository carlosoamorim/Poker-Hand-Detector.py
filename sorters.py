# sorters.py

class SortManager:
    # figures out which sorting algorithm to use based on the user's choice

    @staticmethod
    def sort(cards, algorithm_name):
        if algorithm_name == "merge":
            merge_sort(cards)
        elif algorithm_name == "heap":
            heap_sort(cards)
        elif algorithm_name == "binary":
            binary_insertion_sort(cards)
        elif algorithm_name == "quick":
            quick_sort(cards)
        else:
            raise ValueError(f"Unknown sorting algorithm: {algorithm_name}")


# merge sort:
#best
def merge_sort(cards):
    #  merge sort that splits and merges sorted halfs and sorts them by numeric value ( get_order() )

    if len(cards) > 1:
        mid = len(cards) // 2
        left_half = cards[:mid]
        right_half = cards[mid:]

        # recursively sort both halfs
        merge_sort(left_half)
        merge_sort(right_half)

        # merge the sorted halfs
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].get_order() <= right_half[j].get_order():
                cards[k] = left_half[i]
                i += 1
            else:
                cards[k] = right_half[j]
                j += 1
            k += 1

        # add any remaining elements
        while i < len(left_half):
            cards[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            cards[k] = right_half[j]
            j += 1
            k += 1


# heap sort:

def heap_sort(cards):
    # uses a max heap to sort the cards from biggest to smallest and sorts them by numeric value ( get_order() )

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left].get_order() > arr[largest].get_order():
            largest = left

        if right < n and arr[right].get_order() > arr[largest].get_order():
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(cards)

    # build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(cards, n, i)

    # extract elements from heap, one by one
    for i in range(n - 1, 0, -1):
        cards[i], cards[0] = cards[0], cards[i]  # swap
        heapify(cards, i, 0)


# binary insertion sort:

def binary_insertion_sort(cards):
    # performs insertion sort but uses binary search to find where to insert

    def binary_search(sublist, card, start, end):
        # finds the index where card should be inserted
        while start < end:
            mid = (start + end) // 2
            if card.get_order() < sublist[mid].get_order():
                end = mid
            else:
                start = mid + 1
        return start

    for i in range(1, len(cards)):
        current_card = cards[i]
        # find where to insert current_card in cards[0...i-1]
        pos = binary_search(cards, current_card, 0, i)
        # shift and insert
        for j in range(i, pos, -1):
            cards[j] = cards[j - 1]
        cards[pos] = current_card


# quick sort:
# best O(n log n)
# worst O(n^2)
def quick_sort(cards):
    # sorts using the quick sort method (divide and conquer)

    def _quick_sort(cards, low, high):
        if low < high:
            pi = partition(cards, low, high)
            _quick_sort(cards, low, pi - 1)
            _quick_sort(cards, pi + 1, high)

    def partition(cards, low, high):
        pivot = cards[high]
        i = low - 1
        for j in range(low, high):
            if cards[j].get_order() <= pivot.get_order():
                i += 1
                cards[i], cards[j] = cards[j], cards[i]
        cards[i + 1], cards[high] = cards[high], cards[i + 1]
        return i + 1

    _quick_sort(cards, 0, len(cards) - 1)
