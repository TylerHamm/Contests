def solution(s):
    # Your code here
    
    # Double pointer method
    # Idea, sequences have to start with the same color, I will assume
    # That i can loop to find the indexes of that color
    # I can then increment from there checking to make sure it is the same
    p_1 = 0
    p_2 = 1
    starting_char = s[0]
    curr_seq = ''
    final_seq_len = 0

    while(not final_seq_len and p_2 < len(s)):
        compare_char = s[p_2]
        
        # Check if p_1 and p_2 are the same
        if s[p_1] == s[p_2]:
            failed = False

            # Grab the current assumed sequence
            curr_seq = s[0:p_2]
            curr_seq_len = len(curr_seq)

            # From here, I want to increment by the length and validate the sequences
            # Are the same throughout
            for i in range(curr_seq_len, len(s)-curr_seq_len+1, curr_seq_len):
                new_seq = s[i:i+curr_seq_len]
                if new_seq != curr_seq:
                    failed = True
                    break

            # Validate that the pie is perfectly cut
            if not failed and int(len(s) % curr_seq_len) == 0:
                final_seq_len = int(len(s)/curr_seq_len)
        
        #Increment second pointer
        p_2 += 1

    print(final_seq_len)
    return final_seq_len

text = 'asasasasasasasas'
text = 'sasasasasasasa'
text = 'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop'
solution(text)