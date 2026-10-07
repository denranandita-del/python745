#3. **Find the smallest element in a list** without using `min()`.

list1=[2,2,3,4,5,6,6,7,23,23,12,56]
def findsmallest(list1):
    smallest = list1[0]
    largest = 0
    for i in range(len(list1)):
        if (list1[i] <smallest):
            smallest = list1[i]
        if(list1[i]> largest):
            largest =list1[i]

    print(smallest)
    print(largest)

findsmallest(list1)