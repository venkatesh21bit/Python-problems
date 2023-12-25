""" 1. Create a text file named "number_power_product.txt" with the following content:
2 3 4 2 5 4 3 2 6 3
2. Write a Python program to read these numbers from the file and store them in a list. (2)
3. Implement a recursive function compute_power_recursive() that takes two arguments 
(base and exponent) and computes the power of a number. Use the 
compute_power_recursive() function to calculate the powers using the even positions 
(0, 2, 4, ...) as bases and odd positions (1, 3, 5, ...) as exponents from the list obtained 
in step 2. (3.5)
4. Implement another recursive function compute_product_recursive() that takes two 
arguments (multiplicand and multiplier) and computes their product. Use the 
compute_product_recursive() function to find the product of numbers using the even 
positions (0, 2, 4, ...) as multiplicands and odd positions (1, 3, 5, ...) as multipliers from 
the list obtained in step 2. (3.5)
5. Print the original list, the computed powers, and the computed products. (1)1 """



file=open("number_power_product.txt",'w')
file.write('2 3 4 2 5 4 3 2 6 3')
file.close

with open('number_power_product.txt','r') as file:
    LIST=list(map(int,file.read().split()))
    #alt.list=[int(num) for num in file.read().split()]

print(LIST)

def compute_power_recursive(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base*compute_power_recursive(base,exponent-1)
    
def compute_product_recursive(multiplicand,multiplier):
    if multiplier == 0:
        return 0
    elif multiplier == 1:
        return multiplicand
    else:
        return multiplicand + compute_product_recursive(multiplicand,multiplier-1)

computed_powers=[compute_power_recursive(LIST[i], LIST[i+1]) for i in range (0,len(LIST),2)]
computed_product=[compute_product_recursive(LIST[i], LIST[i+1]) for i in range (0,len(LIST),2)]

print(computed_powers)
print(computed_product)
