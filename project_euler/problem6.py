sum_tot = 0
sq_tot = 0

for i in range(1,101):
    sum_tot += i**2
    sq_tot += i

sq_tot = sq_tot**2

print(sq_tot-sum_tot)