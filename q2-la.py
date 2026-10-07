#2. **Find the largest element in a list** without using `max()`.'''

list1 =[12,34,5,3,78,23,67,8,9,7,12]
def findlargest(list1):
    largest = 0
    for i in range(len(list1)):
        if (list1[i] > largest):
            largest = list1[i]
    print(largest)

    
findlargest(list1)