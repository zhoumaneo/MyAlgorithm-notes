# Out-In-place
def qsort1(alist):
    print(alist)
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        return qsort1([ x for x in alist[1:] if x < pivot]) + \
               [pivot] +\
               qsort1([ x for x in alist[1:] if x >= pivot])
unsortedArray = [6,5,3,1,8,7,2,4]
print(qsort1(unsortedArray))



# In-place
# 1> one index for partition
def qsort2(alist, l, u):
    print(alist)
    if l >= u:
        return
    m = l
    for i in range(l+1,u+1):
        if alist[i] < alist[l]:
            m += 1
            alist[m],alist[i] = alist[i],alist[m]
    # sawp between m and l
    alist[m],alist[i] = alist[i],alist[m]
    qsort2(alist,l,m-1)
    qsort2(alist,m+1,u)
print(qsort2(unsortedArray,0,len(unsortedArray)-1))\


# 2>Two-way partition

def qsort3(alist,lower,upper):
    print(alist)
    if lower >= upper:
        return
    pivot = alist[lower]
    left,right = lower+1,upper
    while left <= right
        while left <= right and alist[left] < pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if left > right:
            break
        alist[left],alist[right] = alist[right], alist[left]

