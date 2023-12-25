Subjects=[]
n=int(input())
for i in range (n):
    Sub=input()
    Subjects.append(Sub)
print(Subjects)

    
def longest_subject_name_recursive(Subjects):
   
    if not Subjects:
        return None
    elif len(Subjects) == 1:
        return Subjects[0]
    else:
        first_subject = Subjects[0]
        rest_subjects = Subjects[1:]
        longest_in_rest = longest_subject_name_recursive(rest_subjects)
        return first_subject if len(first_subject) > len(longest_in_rest) else longest_in_rest


longest_subject_name_recursive(Subjects)
