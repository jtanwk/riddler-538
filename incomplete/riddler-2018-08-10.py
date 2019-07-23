# Riddler - Aug 10, 2018
# https://fivethirtyeight.com/features/where-on-earth-is-the-riddler/

# 1. Initialize 100x100 matrix with random 3 colors

import random
import time

width = 30
height = 30

start_time = time.time()

def view(rug):

    new_rug = []

    for row in rug:
        row_str = [str(x) for x in row]
        row_join = ''.join(row_str)
        new_rug.append(row_join)

    print('\n'.join(new_rug))

# 2. Check each line for 4 of the same color in a row

def check_line(input_line):
    '''If input has 4-run, outputs starting index of run and color, else -1'''
    count = 1
    index = -1
    color = None

    for i in range(len(input_line)):

        if i == 0:    # first item
            continue
        elif input_line[i] == input_line[i-1]:  # compares to previous item
            count += 1

            if count == 4:
                color = input_line[i]
                index = i - 3               # index of 1st item of 4-run
                return index, color

    return -1

# 3. For each line that meets #2, check if 4 lines in a row match on color+index

def check_matrix(input_matrix):
    count = 1

    for j in range(len(input_matrix)):

        if j == 0:
            continue
        elif check_line(input_matrix[j]) == -1:
            continue
        elif check_line(input_matrix[j]) == check_line(input_matrix[j - 1]):
            count += 1

            if count == 4:
                return True, j

    return False, 0

# 4. Loop over #1-3 for a large number of random matrices

num_trials = 100
results = [None] * num_trials

for i in range(num_trials):
    rug = [[random.randint(0, 2) for i in range(width)] for j in range(height)]
    results[i] = check_matrix(rug)[0]

    if results[i] == True:
        print(check_matrix(rug)[1])
        view(rug)
        print("")

reject_pct = results.count(True) * 100 / num_trials

print(f"Reject {reject_pct}%")
print(f"Time taken: {time.time() - start_time} s")


#
