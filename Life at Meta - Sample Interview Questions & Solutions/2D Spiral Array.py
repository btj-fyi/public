"""
Question 1: 2D Spiral Array

Find the pattern and complete the function:
int[][] spiral(int n);
where n is the size of the 2D array.

Sample Output:
input = 3
123
894
765

input = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07

input = 8
1 2 3 4 5 6 7 8
28 29 30 31 32 33 34 9
27 48 49 50 51 52 35 10
26 47 60 61 62 53 36 11
25 46 59 64 63 54 37 12
24 45 58 57 56 55 38 13
23 44 43 42 41 40 39 14
22 21 20 19 18 17 16 15
"""


# segment 1,2, and 3, must be stopped
# segments after 3, may continue until the next coordinate is already occupied. Then turn
def spiral(n):
    m = n
    numbers = list(range(1, (m * n) + 1))
    print(numbers)
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    i = 0
    j = 0
    direction = "up"
    segment = 1
    i = 0
    dimension = n - 1
    while True:
        if (segment == 1) and (i <= dimension):
            matrix[0][i] = numbers.pop(0)
            i += 1
        elif segment == 1:
            segment = 2
            i = 1
        if (segment == 2) and (i <= dimension):
            matrix[i][n - 1] = numbers.pop(0)
            i += 1
        elif segment == 2:
            segment = 3
            i = 1
        if (segment == 3) and (i <= dimension):
            matrix[m - 1][(n - 1) - i] = numbers.pop(0)
            i += 1
        elif segment == 3:
            segment = 4
            i = 0
        if segment == 4:
            match direction:
                # add 1 to i, up until none zero value
                case "up":
                    i += 1
                    if matrix[dimension - i][0] == 0:
                        matrix[dimension - i][0] = numbers.pop(0)
                        i += 1
                    if matrix[dimension - i][0] != 0:
                        i -= 1
                        matrix[dimension - i][0] = numbers.pop(0)
                        i = 0
                        direction = "right"
                # add 1 to j, up until none zero value
                case "right":
                    j += 1
                    if matrix[i][dimension - j] == 0:
                        matrix[i][dimension - j] = numbers.pop(0)
                        j += 1
                    if matrix[i][dimension - j] != 0:
                        j -= 1
                        matrix[i][dimension - j] = numbers.pop(0)
                        direction = "down"

                # subtract 1 from i, up until none zero value
                case "down":
                    i -= 1
                    if matrix[dimension + i][j]:
                        matrix[dimension + i][j] = numbers.pop(0)
                    i -= 1
                    if matrix[i][j] != 0:
                        i += 1
                        matrix[dimension + i][j] = numbers.pop(0)
                        direction = "left"
                # subtract 1 from j, up until none zero value
                case "left":
                    j -= 1
                    if matrix[i][j] != 0:
                        j += 1
                        matrix[i][j] = numbers.pop(0)
        if not numbers:
            break
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


spiral(4)
