def Bubble_sort(l, n):
    for i in range(n):
        for j in range(n-1-i):
            if(l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]     

li = list()
n = int(input("Enter the size of list"))

print("Enter ",n," list elements")
for i in range(n):
    li.append(int(input()))

Bubble_sort(li, n)
print(li)
