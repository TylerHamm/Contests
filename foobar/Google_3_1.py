# Partition, number theory
# Use dynamic programming, overlapping sub problems
# similar to coin problem but has a different addition reasoning
# (there isnt really one) You just need to make sure to not include 
# all solutions as you can only use half of the solutions - 1
# this is due to the stipulations that the prior stair might be higher
# and the fact that the staircase must be at least 2 wide.
def solution(n):

    if n == 3:
        return 1

    # Create array to inrease value accordingly by index 
    combinations = [0] * (n+1)
    combinations[0] = 1

    # Loop through the array (besides index 0)
    # This is essentially the amount in the coin change problem
    for amount in range(1, n+1):
        
        # As the "coin" is always 1, we dont actually have to look
        # at another value like that. But, we still need to loop
        # The the array given the amount. We only need to loop 
        # There is also no skipping here since the value is 1.
        # The skip was done prior.
        for p_1 in reversed(range(amount, n+1)):
            # print(p_1)
            # print("amount: {}".format(amount))
            # print("p_1: {}".format(p_1))
            combinations[p_1] += combinations[p_1-amount]
            print(combinations)

    # you have to return -1 of the value there is 1 invalid solution due to 
    # the restriction of needing 2 stairs
    return combinations[n]-1

print(solution(200))