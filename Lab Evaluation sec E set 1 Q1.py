#Read the number of subjects (N) from the user and then read the subject titles (N strings) from the user into a list called ‘Subjects’. After getting the names, perform the following operations as per the instructions given:
#a. Write a Python function to return the lengths of each subject name as a list, when the entire subject name list is given as parameters. Use an additional function to calculate the length of each string. You should not use len() to calculate the 
#length of each string. [7 Marks] [CO2] [ BTL3]
#b. Re-write the second module to calculate the string length using recursion. 
#[Hint: If there is no character remaining in the string, return 0. Otherwise, calculate the length of the string excluding the first character using the same function, add one to the result, and return the value]




def calculate_length_iterative(s):
    length = 0
    for char in s:
        length += 1
    return length

def calculate_length_recursive(s):
    if not s:
        return 0
    else:
        return 1 + calculate_length_recursive(s[1:])


def get_subject_lengths(subjects, length_function):
    return [length_function(subject) for subject in subjects]


n = int(input("Enter the number of subjects: "))


Subjects = []
for i in range(n):
    subject = input(f"Enter subject {i + 1}: ")
    Subjects.append(subject)


subject_lengths_iterative = get_subject_lengths(Subjects, calculate_length_iterative)


subject_lengths_recursive = get_subject_lengths(Subjects, calculate_length_recursive)


print("Subject lengths using iteration:", subject_lengths_iterative)
print("Subject lengths using recursion:", subject_lengths_recursive)

