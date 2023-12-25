import array as ar
a=ar.array('i',[1,5,2,6,2,8])
search=int(input())
for i in range (len(a)):
    if search == a[i]:
        print(i)
    
