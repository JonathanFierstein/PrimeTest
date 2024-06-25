def is_prime(num):
  """
  This function checks if a number is prime.

  Args:
      num: The number to check.

  Returns:
      True if the number is prime, False otherwise.
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def find_primes(last_number):
  """
  This function finds all prime numbers between 1 and the last_number (inclusive).

  Args:
      last_number: The upper limit for finding prime numbers.

  Returns:
      A list of prime numbers found between 1 and last_number.
  """
  primes = []
  for num in range(1, last_number + 1):
    if is_prime(num):
      primes.append(num)
  return primes

"""
if __name__ == "__main__":
  try:
    last_number = int(input("Enter the last number to test (or press Enter to use 100): "))
  except ValueError:
    last_number = 100  # Default value if input is invalid
  primes = find_primes(last_number)
  print("Prime numbers found between 1 and", last_number, "are:", primes)
"""
last_number = 1000000000 #The number to input into find_primes
primes = find_primes(last_number)
print("Prime numbers found between 1 and", last_number, "are:", primes)
