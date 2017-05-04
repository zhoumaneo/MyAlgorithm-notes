class Sort:
    def mergeSort(self,alist):
        if len(alist) <= 1:
            return alist
        mid = len(alist)/2
        left = self.mergeSort(alist[:mid])
        print("left = " + str(left))
        right = self.mergeSort(alist[mid:])
        print("right = " + str(right))
        return self.mergeSortArray(left, right)
    def mergeSortArray(self,A,B):
        sortedArray = []
        l = 0
        r = 0
        while l <len(A) and r < len(B):
            if A[l]<B[r]:
                sortedArray.append(A[l])
                l += 1
            else:
                sortedArray.append(B[r])
                r += 1
        sortedArray += A[l:]
        sortedArray += B[r:]
        return sortedArray