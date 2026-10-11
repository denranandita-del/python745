#6. **Find the second largest distinct number** in a list.


list1=[14,23,45,78,90,90,87,66]
def bubblesort(list1):
    n=len(list1)
    for i in range (n-1):
        for j in range (n-1-i):
            if (list1[j]<list1[j+1]):
                list1[j] ,list1[j+1] =list1[j+1] ,list1[j]
    return list1
print (bubblesort(list1))


if(list1[0]== list1[1]):
    print(list1[2])
else:
    print(list1[1])