#8. **Remove duplicates from a list** while keeping the original order.

num=[12,56,98,45,12,45,8,8,9,9,5,5,3]
n=len(num)
duplicate=[]
for i in range(n):
    if (num[i] not in duplicate):
        duplicate.append(num[i])
print(duplicate)