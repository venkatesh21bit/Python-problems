f = open("file1.txt", "r")
f1 = open("file2.txt", "w")

a = int(f.read())

s = a ** 2

f1.write("The output is "+str(s))

f1.close()
f.close()
