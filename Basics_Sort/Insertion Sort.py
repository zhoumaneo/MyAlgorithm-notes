def InsertionSort(alist):
    for i,item_i in enumerate(alist):
        print(alist)
        index=i
        while index > 0 and alist[index - 1] > item_i:
            alist[index] = alist[index - 1]
            index -= 1
        alist[index] = item_i
    return alist