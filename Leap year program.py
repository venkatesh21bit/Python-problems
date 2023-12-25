x = int(input("ENTER A YEAR"))
if (x % 400 == 0) and (x % 100 == 0):
    print(f"{x} is a leap year")
elif (x % 4 ==0) and (x % 100 != 0):
    print(f"{x} is a leap year")

else:
    print("{} is not a leap year".format(x))
