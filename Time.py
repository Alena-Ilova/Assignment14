for i in range(n):
    i *= i
    if i >= n:
        break


n = 10
for i in range(n):
    print(f"Current i: {i}")
    i *= i
    if i >= n:
        print("Breaking the loop")
        break
        

for i in range(n):
    i = pow(2, i)
    if i > (n + 1):
        break


def complex_method(n):
    for i in range(n):
        print(i, n)
        if n > 1:
            complex_method(n - 1)
        else:
            return True