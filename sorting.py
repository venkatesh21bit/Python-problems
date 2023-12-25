def sort(l):
    global n
    if l.sort()!=l:
        for i in range (n-1):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
    else:            
        return (l)
            
n=int(input())
l=[]
for j in range (n):
    a=int(input())
    l.append(a)
sort(l)
print(l)
