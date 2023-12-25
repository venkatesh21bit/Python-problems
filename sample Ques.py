#You've uncovered a mysterious text file named "number_series.txt" that contains a sequence of ten numbers. This sequence holds a secret, and your mission is to create a Python program that reads these numbers, computes their recursive sum and average using two separate recursive functions, and reveals the hidden patterns within.

#Here's the step-by-step guide for your program:

#Create a text file named "number_series.txt" with the following content:
#12 8 5 10 15 20 25 30 35 40

#1. Write a Python program to read the numbers from the file and store them in a list.

#2. Implement a recursive function compute_recursive_sum that takes a list as input and calculates the sum of its elements. Use the compute_recursive_sum function to find the recursive sum of the numbers obtained in step 2.

#3. Implement another recursive function compute_recursive_average that takes a list, the current index, and the cumulative sum as input and calculates the average of the elements. Use the compute_recursive_average function to find the recursive average of the numbers obtained in step 2.

#4. Print the original list, the recursive sum, and the recursive average.



file=open('numberseries_test','w')
file.write('12 8 5 10 15 20 25 30 35 40')
file.close
file=open('numberseries_test','r')
print(file.read())


def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
        return numbers

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError:
        print(f"Error: Unable to convert all elements to integers in '{file_path}'.")
        return None
    
def compute_recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + compute_recursive_sum(lst[1:])

def compute_recursive_average(lst, index=0, cumulative_sum=0):
    if index == len(lst):
        if len(lst) == 0:
            return 0
        return cumulative_sum / len(lst)
    return compute_recursive_average(lst, index + 1, cumulative_sum + lst[index])


file_path = "numberseries_test"
numbers = read_numbers_from_file(file_path)

if numbers is not None:
   
    recursive_sum = compute_recursive_sum(numbers)

    
    recursive_average = compute_recursive_average(numbers)

    
    print("Original list:", numbers)
    print("Recursive sum:", recursive_sum)
    print("Recursive average:", recursive_average)
