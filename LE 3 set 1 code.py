file=open('magic_numbers.txt','w')
file.write('123456 234567 345678 456789 567890 678901 789012 890123 901234 123789')
file.close


def compute_recursive_sum(numbers):
    if not numbers:
        return 0
    else:
        return int(numbers[0]) + compute_recursive_sum(numbers[1:])


with open("magic_numbers.txt", "r") as file:
    numbers_list = file.read().split()

recursive_sum = compute_recursive_sum(numbers_list)
print(f"Recursive sum of magical numbers: {recursive_sum}")

def compute_power_sum(number):
    if number < 10:
        return number
    else:
        digit = number % 10
        position = len(str(number)) - 1
        return digit ** position + compute_power_sum(number // 10)

power_sum = compute_power_sum(recursive_sum)
print(f"Power sum of digits in the recursive sum: {power_sum}")
