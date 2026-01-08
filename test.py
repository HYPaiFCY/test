def quick_sort(arr):
    """快速排序算法"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


# 示例使用
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("原数组:", arr)
    print("排序后:", quick_sort(arr))