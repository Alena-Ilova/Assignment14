def sum_digits(n):

 if n == 0:
  return 0
 else:
  return n % 10 + sum_digits(n // 10)

number = 53872
sum_of_digits = sum_digits(number)
print(f"The sum of digits in {number} is {sum_of_digits}")