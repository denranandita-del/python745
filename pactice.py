#3. **Find the smallest element in a list** without using `min()`.

list1= [12,23,45,56,78,1,14,24]
smallest = list1[0]

for i in range(len(list1)):
    if (list1[i] < smallest):
        smallest = list1[i]
print(smallest)
