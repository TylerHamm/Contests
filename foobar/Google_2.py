import itertools
def solution(l):
    # Your code here

    # l = sorted(l, reverse=True)

    # l_perm = list(itertools.permutations(l))

    l_perm_full = []

    # take the range of each number index
    # Start with 1 as you dont need 0 length tuples
    for i in range(1, len(l)+1):  
        #permutate off each one, with i length tuples
        for perm in itertools.permutations(l, i):
            l_perm_full.append(perm)

    largest = 0

    for lst in l_perm_full:
        string_ints =  [str(int) for int in lst]
        print(''.join(string_ints))
        lst_int = int(''.join(string_ints))
        if lst_int % 3 == 0:
            if lst_int > largest:
                largest = lst_int

    print(largest)

    return largest

solution([3,1,4,1,5,9])