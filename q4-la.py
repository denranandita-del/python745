#4. **Reverse a list** without using `reverse()` or slicing.

list1 =[22,12,3,32,1,2,3,14,45,56,9]
rev = []
n=len(list1)
  
for i in range (len(list1)):
    rev.append(list1[n-i-1])
print(rev)
