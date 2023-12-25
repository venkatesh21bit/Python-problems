n = int(input("Enter the size of the sequence"))

l = []

for i in range(n):
    l.append(int(input()))

key = int(input("Enter the search key"))

flag = False

for i in range(n):
    if(key == l[i]):
        flag = True
        print("The key is found at index ", i)
        break
else:
    print("The key is not found")

    
