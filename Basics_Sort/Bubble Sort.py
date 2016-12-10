def bubbleSort(alist):
    for i in range(len(alist)):
        print(alist)
        for j in range(1,len(alist)-i):
            if alist[j-1]>alist[j]:
                alist[j-1],alist[j] = alist[j],alist[j-1]
    return alist
unsorted = [1,6,5,2,8]
print(bubbleSort(unsorted))
