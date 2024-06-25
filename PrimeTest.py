import time

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


last_number = 100000000#The number to input into find_primes

start_time = time.time()  # Record start time
primes = find_primes(last_number)
end_time = time.time()  # Record end time
elapsed_time = end_time - start_time #Computer difference between start time and end time
numberofprimes = len(primes)
print("Prime numbers found between 1 and", last_number, "are:", primes)
print("A total of ", numberofprimes, " prime numbers were found between 1 and ", last_number, ".")
print(f"Found {numberofprimes} prime numbers in {elapsed_time:.2f} seconds.")