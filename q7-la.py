#7. **Find the second smallest distinct number** in a list.

num=[12,34,56,78,90,87,65,43,32,1,1]
# def secondsmllest(num):
#     n=len(num)
#     for i in range (n-1):
#         for j in range(n-i-1):
#             if (num[j] > num[j+1]):
#                 num[j], num[j+1] = num[j+1], num[j]
#     return num
# print(secondsmllest(num))

# if (num[0]==num[1]):
#     print(num[2])
# else:
#     print(num[1])

n= len(num)
for i in range (n-1):
    for j in range(n-i-1):
        if (num[j] > num[j+1]):
            num [j] , num [j+1] = num[j+1] , num[j]

print(num)
print(num[1])
# if (num[0] == num[1]):
#     print(num[2])
# else:
#     print(num[1])