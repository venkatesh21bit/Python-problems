def BinSearch(li, l, h, k):
    if(l <= h):
        m = (l+h)//2
        if(k == li[m]):
            return m
        elif(k < li[m]):
            return BinSearch(li, l, m-1, k)
        else:
            return BinSearch(li, m+1, h, k)
li = list()
n = int(input("Enter the size of your list"))
print("Enter the ", n, " list elements")

for i in range(n):
    li.append(int(input()))

k = int(input("Enter the key to be searched for"))

pos = BinSearch(li, 0, n-1, k)

if(pos!= None):
    print("The search key is found at ", pos)
else:
    print("The search key is not found")
