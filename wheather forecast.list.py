
temp_data = []


n = int(input("How many days of data do you want to enter? "))


for i in range(n):
    temp = float(input(f"Enter the temperature for day {i+1}: "))
    temp_data.append(temp)


print(f"The temperature data is: {temp_data}")


def max_index(lst):
    
    max_elem = lst[0]
    max_idx = 0

    
    for i in range(1, len(lst)):
        if lst[i] > max_elem:
            
            max_elem = lst[i]
            max_idx = i
    
   
    return max_idx


def min_index(lst):
    
    min_elem = lst[0]
    min_idx = 0

   
    for i in range(1, len(lst)):
        if lst[i] < min_elem:
           
            min_elem = lst[i]
            min_idx = i
    
    
    return min_idx


warmest_day = max_index(temp_data) + 1
coldest_day = min_index(temp_data) + 1


print(f"The warmest day is day {warmest_day} with a temperature of {temp_data[warmest_day-1]} degrees.")
print(f"The coldest day is day {coldest_day} with a temperature of {temp_data[coldest_day-1]} degrees.")
