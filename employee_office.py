stud1_course = {'A', 'B', 'C'}
stud2_courses = {'B', 'C', 'D'}
stud3_courses = {'C', 'D', 'E'}


def find_common_courses(set1, set2):
    return set1.intersection(set2)


def find_unique_courses(set1, set2):
    return set1.symmetric_difference(set2)


def find_all_courses(set1, set2, set3):
    return set1.union(set2, set3)


common_courses_1_2 = find_common_courses(student_1_courses, student_2_courses)
unique_courses_1_2 = find_unique_courses(student_1_courses, student_2_courses)
all_courses = find_all_courses(student_1_courses, student_2_courses, student_3_courses)

print(f"Common courses between Student 1 and Student 2: {common_courses_1_2}")
print(f"Unique courses between Student 1 and Student 2: {unique_courses_1_2}")
print(f"All unique courses across all students: {all_courses}")
4
