original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def divide_and_conquer(arr, start, end):
    # base case
    if start == end:
        return arr[start]

    # find middle index
    mid = (start + end) // 2

    # Conquer: recursively find the maximum in each half
    max_left = divide_and_conquer(arr, start, mid)
    max_right = divide_and_conquer(arr, mid + 1, end)
    # The combine both halves
    return max(max_left, max_right)


result = divide_and_conquer(original_list, 0, len(original_list) - 1)

print("The maximum element in the array is:", result)
