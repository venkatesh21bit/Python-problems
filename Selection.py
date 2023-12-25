def Selection_sort(l, n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if(l[j] < l[min]):
                min = j
        l[i], l[min] = l[min], l[i]

li = list()
n = int(input("Enter the size of list"))

print("Enter ",n," list elements")
for i in range(n):
    li.append(int(input()))

Selection_sort(li, n)
