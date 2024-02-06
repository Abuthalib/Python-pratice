def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_hand = arr[:mid]
        right_hand = arr[mid:]

        merge_sort(left_hand)
        merge_sort(right_hand)

        i = j = k = 0

        while i < len(left_hand) and j < len(right_hand):
            if left_hand[i] < right_hand[j]:
                arr[k] = left_hand[i]
                i += 1
            else:
                arr[k] = right_hand[j]
                j += 1
            k += 1

        while i < len(left_hand):
            arr[k] = left_hand[i]
            i += 1
            k += 1

        while j < len(right_hand):
            arr[k] = right_hand[j]
            j += 1
            k += 1

arr = [3, 4, 1, 6, 2, 7, 1, 9, 2, 8]
merge_sort(arr)
print(arr)
