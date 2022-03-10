import random
import statistics


"""
quicksort with median as pivot
Everything less than pivot is split into left half of list, everything larger than pivot goes to right half of the list
"""
#splits lists into merge function
def quicksort(list):
    "Null"

    left = []
    right = []
    midpt = []


    if len(list) <= 1:
        return list

    if len(list) == 2:
        if list[0] > list[1]:
            a = list[0]
            list[0] = list[1]
            list[1] = a
        return list

    midpt.append(statistics.median_high(list))

    #if list is larger than two, perform pivot of list
    for i in range(0,len(list),1):
        if list[i] <= midpt[0]:
            left.append(list[i])
        else:
            right.append(list[i])

    #Exemption for when midpoint is repeated and the highest value of a particular string so recursion
    #doesn't continue endlessly
    if len(list) == len(left):
        right.append(left[len(left)-1])
        left.pop(len(left)-1)


    left = quicksort(left)
    right = quicksort(right)

    new_list = left + right


    return new_list

"""
FOR TESTING PURPOSES
#generate random list
test_list = []



for i in range(0,10,1):
    test_list.append(random.randrange(0,100))
print(test_list)

processed_list = quicksort(test_list)
print(processed_list)

#Example of a list that would create an exemption of endless recursion, midpoint of 3,10,10 is 10 and creates no right list
break_list = [99,87,30,3,10,82,54,11,10,56]
print(quicksort(break_list))



"""
