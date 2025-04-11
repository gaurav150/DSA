'''
You are given a table with 
 rows and 
 columns. Each cell is colored with white or black. 
 Considering the shapes created by black cells, 
 what is the maximum border of these shapes? 
 Border of a shape means the maximum number of consecutive black cells in any row or column without any white cell in between.

A shape is a set of connected cells. Two cells are connected if they share an edge. Note that no shape has a hole in it.

Input format

The first line contains 
 denoting the number of test cases.
The first line of each test case contains integers 
 denoting the number of rows and columns of the matrix. Here, '#' represents a black cell and '.' represents a white cell. 
Each of the next 
 lines contains 
 integers.

'''


def max_consecutive_hash(line):
    max_count = count = 0
    for ch in line:
        if ch == '#':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

# Main
num_of_testcases = int(input())

for _ in range(num_of_testcases):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    max_border = 0

    # Check rows
    for row in grid:
        max_border = max(max_border, max_consecutive_hash(row))

    # Check columns
    for col in zip(*grid):  # Transpose to get columns
        max_border = max(max_border, max_consecutive_hash(col))

    print(max_border)

# EXAMPLE 
''' this is input

10
2 15
.....####......
.....#.........
7 9
...###...
...###...
..#......
.####....
..#......
...#####.
.........
18 11
.#########.
########...
.........#.
####.......
.....#####.
.....##....
....#####..
.....####..
..###......
......#....
....#####..
...####....
##.........
#####......
....#####..
....##.....
.#######...
.#.........
1 15
.....######....
5 11
..#####....
.#######...
......#....
....#####..
...#####...
8 13
.....######..
......##.....
########.....
...#.........
.............
#######......
..######.....
####.........
7 5
.....
..##.
###..
..##.
.....
..#..
.#...
14 2
..
#.
..
#.
..
#.
..
..
#.
..
..
..
#.
..
7 15
.###########...
##############.
...####........
...##########..
.......#.......
.....#########.
.#######.......
12 6
#####.
###...
#.....
##....
###...
......
.##...
..##..
...#..
..#...
#####.
####..
'''


''' this is output
4
5
9
6
7
8
3
1
14
5
'''