#6. **Find the second largest distinct number** in a list.

Number=[12,23,4,5,2,3,5,12,5,23,87,89]
def findlargest(list1):
    largest = 0
    for i in range(len(list1)):
        if (list1[i] > largest):
            largest = list1[i]
    print(largest)

    
findlargest(list1)