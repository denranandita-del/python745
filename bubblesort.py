


def bubblesort(list1):
    n=len(list1)
    for i in range (n-1):
        for j in range (n-1-i):
            if (list1[j]>list1[j+1]):
                list1[j] ,list1[j+1] =list1[j+1] ,list1[j]
    return list1

list1=[14,23,45,78,90,90,87,66]
print (bubblesort(list1))