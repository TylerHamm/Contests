# from math import ceil as c
# from math import floor as fl

# def curr_arr_mod(arr, width, loop):
#     print('curr_arr_mod')
#     print(arr)
#     print(width)
#     print(loop)
#     for i in reversed(range(1, width)):
#         arr[i] += loop
#     arr[0] -= (width - 1)
#     print(arr)
#     return arr

# def build_start_array(width, n):
#     retval = [None] * width
#     curr_height_count = 1
#     total_sub = 0
#     for i in reversed(range(1, width)):
#         retval[i] = curr_height_count
#         curr_height_count += 1
#         total_sub += i
#     retval[0] = n - total_sub

#     return retval

# def solution(n):
#     # Your code here

#     # starting_array = [n-1, n]

#     curr_n = 0
#     curr_add = 0
#     max_stairs = 0

#     # min_height of each stair equals index of the value

#     # This shouldn't be passed based on input max input of 200
#     # It can only have 14 stairs
#     # Sub height keeps track of the amount to subtract at each 
#     # stair width.
#     sub_height = [None] * 14

#     # Get some base data to mess with
#     while(True):
#         curr_n += max_stairs
#         max_stairs += 1
#         if curr_n > (n-curr_n):
#             break

#     variation_count = 0

#     stair_height = None
    
#     # print('max_stairs: {}'.format(max_stairs))
#     for width in range(2, max_stairs+1):
#         stair_height = build_start_array(width, n)
# # 
#         # Loop Through the columns
#         for focus in range(1, width):
#             loop = 0
#             curr_arr_base = stair_height.copy()
#             curr_arr = curr_arr_base.copy()
            
#             while(curr_arr[0] > curr_arr[1]+focus+2):
#                 while(curr_arr[0] > curr_arr[1]):
#                     variation_count += 1
#                     curr_arr[0] -= 1
#                     curr_arr[1] += 1
#                 loop += 1
#                 curr_arr = curr_arr_mod(curr_arr_base, width, loop)

#                 print('{} : {}'.format(curr_arr[0], curr_arr[1]+focus+2))

#     return variation_count

# count = solution(200)
# print(count)

def answer(n):
    # make n+1 coefficients
    coefficients = [1]+[0]* n
    #go through all the combos
    for i in range(1, n+1):
        #start from the back and go down until you reach the middle
        for j in range(n, i-1, -1):
            print(j)
            coefficients[j] += coefficients[j-i]
    return coefficients[n] - 1

print(answer(10))