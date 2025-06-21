def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def selection_sort(nums):
    n = len(nums)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        current_index = i
        while current_index > 0 and nums[current_index - 1] > nums[current_index]:
            nums[current_index], nums[current_index - 1] = nums[current_index - 1], nums[current_index]
            current_index -= 1
    return nums


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    left = nums[:len(nums) // 2]
    right = nums[len(nums) // 2:]
    left_side = merge_sort(left)
    right_side = merge_sort(right)
    final = []
    i = j = 0
    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            final.append(left_side[i])
            i += 1
        else:
            final.append(right_side[j])
            j += 1
    final.extend(left_side[i:])
    final.extend(right_side[j:])
    return final


def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1
