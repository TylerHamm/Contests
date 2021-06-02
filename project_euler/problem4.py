
def is_pal(num):
    p_1 = 0
    p_2 = len(num) -1
    while p_2 > p_1:
        if num[p_1] != num[p_2]:
            return False
        p_2 -= 1
        p_1 += 1

    return True

def is_three_digit(num):
    for i in range(999, 100, -1):
        print(num, i)
        if num/i > 1000:
            return False
        elif num % i == 0:
            print(num/i)
            return True

max = 998100
min = 10000

for i in range(max, min, -1):
    if is_pal(str(i)):
        if is_three_digit(i):
            print(i)
            exit(1)