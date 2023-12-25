li = list()
n = int(input("Enter the size of your list"))
print("Enter the ", n, " list elements")

for i in range(n):
    li.append(int(input()))

k = int(input("Enter the key to be searched for"))

l = 0
h = n-1

while(l <= h):
    m = (l+h)//2
    if(k == li[m]):
        print("The key is found at ", m)
        break
    elif(k < li[m]):
        h = m - 1
    else:
        l = m + 1

else:
    print("The search is not found")
