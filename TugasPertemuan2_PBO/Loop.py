num = 17
is_prime = True
i = 2

while i * i <= num:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(num, "adalah bilangan prima.")
else:
    print(num, "bukan bilangan prima.")
