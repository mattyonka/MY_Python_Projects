def linear_search(list,target):
    #returns index position of target if found, else returns none

    for i in range(0,len(list),1):
        if list[i] == target:
            return i
    return None

def binary_search(list,target):
    first = 0
    last = len(list)-1
    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        elif list[midpoint] > target:
            last = midpoint - 1
    return None




testList = [0,1,2,3,4,5,6,7,8,9,10]
testTarget = 9

a = linear_search(testList,testTarget)
print(a)

b = binary_search(testList,testTarget)
print(b)


