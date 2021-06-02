li = list(range(1,20))

current = 0
inc = 20
while True:
    # print(current)
    current += inc

    success = True
    for i in reversed(li):
        if current % i != 0:
            success = False
            break
    
    if success:
        break

print(current)
