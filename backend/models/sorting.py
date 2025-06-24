def bubble_sort(nums):
    steps = [nums[:]]
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                steps.append(nums[:])
    return steps


def selection_sort(nums):
    steps = [nums[:]]
    n = len(nums)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        steps.append(nums[:])
    return steps


def insertion_sort(nums):
    steps = [nums[:]]
    n = len(nums)
    for i in range(1, n):
        current_index = i
        while current_index > 0 and nums[current_index - 1] > nums[current_index]:
            nums[current_index], nums[current_index - 1] = nums[current_index - 1], nums[current_index]
            current_index -= 1
            steps.append(nums[:])
    return steps


def merge_sort(nums, steps=None):
    if steps is None:
        steps = [nums[:]]

    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid], steps)
    right = merge_sort(nums[mid:], steps)

    final = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
    final.extend(left[i:])
    final.extend(right[j:])

    nums[:] = final
    steps.append(nums[:])
    return nums  # still return the sorted array


def quick_sort(nums, low, high, steps=None):
    if steps is None:
        steps = [nums[:]]
    if low < high:
        mid = partition(nums, low, high, steps)
        quick_sort(nums, low, mid - 1, steps)
        quick_sort(nums, mid + 1, high, steps)
    return steps


def partition(nums, low, high, steps):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            steps.append(nums[:])
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    steps.append(nums[:])
    return i + 1
