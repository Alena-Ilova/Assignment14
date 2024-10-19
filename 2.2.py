def sum_up_to(n):

 if n == 0:
  return 0
 else:
  return n + sum_up_to(n - 1)

number = 538
sum_of_numbers = sum_up_to(number)
print(f"The sum of numbers from 0 to {number} is {sum_of_numbers}")