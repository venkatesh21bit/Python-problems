print('Enter the no. of days of weather')
n=int(input())
print('Enter the values')
L=list(map(int, input().split()))
l=L
for i in range (n-1):
    if L[i]>L[i+1]:
        L[i],L[i+1] = L[i+1],L[i]
print(L)
print('Type 1 to show the warmest day')
print('Type 2 to show the coldest day')
y=int(input())
a=l.index(L[0])
b=l.index(L[n-1])
if y==1:
    print('DAY',b+1)
    print(L[n-1])
if y==2:
    print('DAY',a+1)
    print(L[0])
