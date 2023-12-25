def Insertion(l, n):
    for i in range(1, n):
        key = l[i]
        j = i-1

        while(j >= 0 and l[j] > key):
            l[j+1] = l[j]
            j = j - 1
        l[j+1] = key
        print("Pass ", i)
        print(l)


li = list()
n = int(input("Enter the size of list"))

print("Enter ",n," list elements")
for i in range(n):
    li.append(int(input()))

Insertion(li, n)
print(li)
