def insert_sort(arr):
    n=len(arr)
    # 插入排序的精髓：对于每一个数，都在左边已经排好序的序列里找其对应的位置，第一个不用找，第二个开始，总共找n-1次
    for i in range(1,n):
        temp=arr[i]
        # 每个个选定的要插入的数，它的索引是几就最多需要和左边的已经排号的序列就行比较几次，索引为3的数（第四个）需要和前面三个都进行比较
        for j in range(0,i):
            # 如果出现前面的数大于后面的数则将两个进行换位，temp永远都是选定的要插入的数
            if temp<arr[i-j-1]:
                arr[i - j] =arr[i-j-1]
                arr[i-j-1]=temp
    return arr

arr=[1,3,5,2,6,8,2,9]
print(insert_sort(arr))

