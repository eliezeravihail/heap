import heap as H

def heapSort(arr):          
    heap = H.heap()
    for i in arr:
        heap.push(i)
    for i in range(len(arr)):
        arr[len(arr)-1-i] = heap.popMax()
        
"""#use:
x= [23,2,454,6,8787,3]   
heapSort(x)
print(x)


#======== output: =============
[2, 3, 6, 23, 454, 8787]
"""
