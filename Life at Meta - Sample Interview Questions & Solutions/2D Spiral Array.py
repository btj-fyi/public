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
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    print(matrix)
    numbers = list(range(1, (n * n) + 1, 1))
    print(numbers)
    i = 0
    j = 0
    row = 0
    col = 0
    c = 0
    if c == 0:
        # go right, length
        for x in range(0, n, 1):
            j = x
            matrix[i][j] = numbers.pop(0)
        c += 1
        row, col = i, j
        print(i, j)
    if c == 1:
        # go down, length-1
        for x in range(row + 1, n, 1):
            i = x
            matrix[i][j] = numbers.pop(0)
        c += 1
        row, col = i, j
        print(i, j)
    if c == 2:
        # go left, length-1
        for x in range(col - 1, -1, -1):
            j = x
            matrix[i][j] = numbers.pop(0)
        c += 1
        row, col = i, j
        print(i, j)
        direction = "up"
    if c > 2:
        while True:
            match direction:
                case "up":
                    # go up, till none zero
                    i -= 1
                    if matrix[i][j] == 0:
                        matrix[i][j] = numbers.pop(0)
                    else:
                        i += 1
                        direction = "right"
                case "right":
                    # go right
                    j += 1
                    if matrix[i][j] == 0:
                        matrix[i][j] = numbers.pop(0)
                    else:
                        j -= 1
                        direction = "down"
                case "down":
                    # go down
                    i += 1
                    if matrix[i][j] == 0:
                        matrix[i][j] = numbers.pop(0)
                    else:
                        i -= 1
                        direction = "left"
                case "left":
                    # go left
                    j -= 1
                    if matrix[i][j] == 0:
                        matrix[i][j] = numbers.pop(0)
                    else:
                        j += 1
                        direction = "up"
            if not numbers:
                break


spiral(8)
