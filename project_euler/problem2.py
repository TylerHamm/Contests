max = 4000000
current = 0
p_1 = 1
p_2 = 2
retval = 2

while p_2 < max:
    current = p_1 + p_2
    p_1 = p_2
    p_2 = current

    if p_2 % 2 == 0:
        retval += p_2

print(retval)
