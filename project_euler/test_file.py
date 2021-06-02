import sys

max_x = 0
max_y = 0

table = []
up_s = []
right_s = []
down_s = []
left_s = []

def reset_values():
    global max_x
    global max_y
    global table
    global up_s
    global right_s
    global down_s
    global left_s

    max_x = 0
    max_y = 0

    table = []
    up_s = []
    right_s = []
    down_s = []
    left_s = []

def count_i(y, x):
    if x>=2 and y>=2:
        return min(x//2,y) + min(y//2,x) - 2
    else:
        return 0

def valid_coord(y, x):
    if y < 0 or x < 0 or y > max_y or x > max_x:
        return False
    return True

def fill_down(y, x):
    global down_s

    count = 1
    while valid_coord(y,x):
        if down_s[y][x] >= 1:
            down_s[y][x] = count
            count += 1
        else:
            count = 1
        y -= 1
    return

def fill_right(y, x):
    global right_s
    
    count = 1
    while valid_coord(y,x):
        if right_s[y][x] >= 1:
            right_s[y][x] = count
            count += 1
        else:
            count = 1
        x -= 1
        
    return

def fill_up(y, x):
    global up_s
    
    count = 1
    while valid_coord(y,x):
        if up_s[y][x] == 1:
            up_s[y][x] = count
            count += 1
        else:
            count = 1
        y += 1
    return

def fill_left(y, x):
    global left_s
    
    count = 1
    while valid_coord(y,x):
        if left_s[y][x] == 1:
            left_s[y][x] = count
            count += 1
        else:
            count = 1
        x += 1
    return

count = int(sys.stdin.readline())

case_num = 1
for _ in range(0,count):
    reset_values()
    max_y, max_x = sys.stdin.readline().rstrip().split(" ")
    
    max_y = int(max_y) - 1
    max_x = int(max_x) - 1


    for _ in range(max_y+1):
        line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        table.append(line)

        up_s.append(line.copy())
        right_s.append(line.copy())
        down_s.append(line.copy())
        left_s.append(line.copy())

    def fill_tables():
        for y, row in enumerate(table):
            for x, column in enumerate(row):
                fill_up(y,x)
                fill_right(y,x) 
                fill_down(y,x)
                fill_left(y,x)

    fill_tables()
    retval = 0
    for y in range(0, len(table)):
        for x in range(0, len(table[0])):
            retval += count_i(up_s[y][x], right_s[y][x])
            retval += count_i(up_s[y][x], left_s[y][x])
            retval += count_i(down_s[y][x], right_s[y][x])
            retval += count_i(down_s[y][x], left_s[y][x])

    print("Case #{}: {}".format(case_num, retval))
    case_num += 1