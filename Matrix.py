import numpy as np
import random
def backtrace(first, second, matrix):
    f = [char for char in first]
    s = [char for char in second]
    new_f, new_s = [], []
    row = len(f)
    col = len(s)
    trace = [[row, col]]

    while True:
        a = matrix[row - 1][col]
        b = matrix[row - 1][col - 1]
        c = matrix[row][col - 1]

        which = min(a, b, c)

        if which == matrix[row][col] or which == matrix[row][col] - 2:
           
            trace.append([row - 1, col - 1])
            new_f = [f[row - 1]] + new_f
            new_s = [s[col - 1]] + new_s

            row, col = row - 1, col - 1

        elif which == matrix[row][col] - 1:
           
            if which == matrix[row - 1][col]:
                trace.append([row - 1, col])
                new_f = [f[row - 1]] + new_f
                new_s = ["-"] + new_s

                row, col = row - 1, col

            elif which == matrix[row][col - 1]:
                trace.append([row, col - 1])
                new_f = ["-"] + new_f
                new_s = [s[col - 1]] + new_s

                row, col = row, col - 1

       
        if row == 0 or col == 0:
            return trace, new_f, new_s
        
        
def word_edit_distance(x, y):
    rows = len(x) + 1
    cols = len(y) + 1
    distance = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            if x[row - 1] == y[col - 1]:
                cost = 0
            else:
                cost = 2
            distance[row][col] = min(distance[row - 1][col] + 1,
                                     distance[row][col - 1] + 1,
                                     distance[row - 1][col - 1] + cost)
     

    edit_distance = distance[row][col]
    return edit_distance, distance



 
random_string = '' 
random_string1=""
for _ in range(10):
   
    random_integer = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
   
    random_integer = random_integer - 32 if flip_bit == 1 else random_integer

    random_string += (chr(random_integer))
for _ in range(10):
   
    random_integer1 = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
   
    random_integer1 = random_integer1 - 32 if flip_bit == 1 else random_integer1

    random_string1 += (chr(random_integer1))    
 
print(random_string, len(random_string))
a=random_string
b=random_string1 
result = word_edit_distance(a,b)
print(result[0])
print(result[1])
print(backtrace(random_integer,random_integer1 , result))