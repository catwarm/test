def quicksort(arr):
        """
        对数组进行快速排序
        param arr: 待排序数组
        return: 排序后的数组
        """
        # 如果数组为空或只有一个元素，则直接返回
        if len(arr) <= 1:
            return arr
                                            
        # 选择一个基准元素（这里选择数组的第一个元素）
        pivot = arr[0]
                                                        
        # 创建两个子数组，一个存放小于基准的元素，一个存放大于基准的元素
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
                                                                        
                                                                        
        # 递归地对两个子数组进行快速排序，并合并结果
        return quicksort(less) + [pivot] + quicksort(greater)
# 示例使
arr = [10, 7, 8, 9, 1, 5]
print("排序前的数组:", arr)
sorted_arr = quicksort(arr)
print("排序后的数组:", sorted_arr)