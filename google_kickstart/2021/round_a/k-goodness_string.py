import sys

def get_g_score(w):
    p_1 = 0
    p_2 = len(w) - 1
    c = 0

    while p_2 > p_1:
        
        if w[p_1] != w[p_2]:
            c += 1

        p_1 += 1
        p_2 -= 1
    
    return c



test_num = 1
count = int(sys.stdin.readline())

for _ in range(0,count):
    n, k = sys.stdin.readline().rstrip().split(" ")
    word = sys.stdin.readline().rstrip()
    
    n = int(n)
    k = int(k)

    if len(word):
        g_score = get_g_score(word)
        combos = n/2

        result =  abs(g_score - k)
    else:
        result = 0

    print('Case #{}: {}'.format(test_num, result))
    test_num += 1