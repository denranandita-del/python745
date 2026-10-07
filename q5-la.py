#5. **Count how many even and odd numbers** are present in a list.

list1 =[22,12,3,32,1,2,3,14,45,56,9]

count=0

for i in range(len(list1)):
    if (i % 2 == 0):
       count +=1

print("Total even number:",count)
print("Total odd number: ",len(list1)-count)
