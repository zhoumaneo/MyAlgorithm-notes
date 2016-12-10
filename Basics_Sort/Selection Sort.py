def SelectionSort(alist):
    for i in range(len(alist)):
        print(alist)
        min_index = i
        for j in range(i+i,len(alist)):
            if alist[j]<alist[min_index]:
                min_index = j
        alist[min_index],alist[i] = alist[i],alist[min_index]
    return alist