n = int(input("Enter the size of the sequence"))

l = []

for i in range(n):
    l.append(int(input()))

key = int(input("Enter the search key"))

flag = False

count = 0

for i in range(n):
    if(key == l[i]):
        flag = True
        count += 1

print("The number of times matches are found is ", count)



    
