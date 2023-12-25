# Function to count the number of digits in a given number
def count_digits(n):
  count = 0
  while n > 0:
    count += 1
    n //= 10
  return count

# Function to check if a given number is a Disarium number
def is_disarium(n):
  # Get the number of digits
  digits = count_digits(n)
  # Initialize the sum
  sum = 0
  # Loop through the digits from right to left
  while n > 0:
    # Get the rightmost digit
    d = n % 10
    # Add the digit raised to the power of its position
    sum += d ** digits
    # Decrease the position by 1
    digits -= 1
    # Remove the rightmost digit
    n //= 10
  # Return True if the sum is equal to the original number, False otherwise
  return sum == n

# Get the input from the user
n = int(input("Enter a number: "))
# Check if the number is a Disarium number
if is_disarium(n):
  print(n, "is a Disarium number")
else:
  print(n, "is not a Disarium number")
