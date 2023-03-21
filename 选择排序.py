def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        temp=arr[i]
        min_index=i

        # 从剩下的值里找出最小的值，并且把值赋给temp
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                temp=arr[j]
                min_index=j

        # 将找到最小的值与最左边的值交换
        arr[min_index]=arr[i]
        arr[i]=temp
    return arr


def selection_reverse_sort(arr):
    n=len(arr)
    for i in range(n-1):
        temp=arr[i]
        max_index=i
        for j in range(i+1,n):
            if arr[max_index]<arr[j]:
                temp=arr[j]
                max_index=j
        arr[max_index]=arr[i]
        arr[i]=temp
    return arr


arr=[3,4,2,5,1,6]
print(selection_sort(arr))
print(selection_reverse_sort(arr))