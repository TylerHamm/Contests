target = 600851475143
prime_numbers = []
i = 0
current = target
retval = []

lower = 2
upper = 10000

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime_numbers.append(num)

while current > 1:
    if current in prime_numbers:
        retval.append(current)
        current = 1
        break
    
    for num in prime_numbers[i::]:
        print(num)
        if current % num == 0:
            retval.append(num)
            current /= num
        else:
            i+=1
    
print(retval)