#!/usr/bin/python
from collections import deque


def Answer_P(solution):
    total_modified = 0
    print('List of cell locations modified:')
    curr_row = 0
    for key in sorted(solution.keys()):
        x, y = key
        if x != curr_row:
            print()
            curr_row = x
        print(key, end=',')
        total_modified += 1
    print()
    print()
    print('Number of cells modified:', total_modified)


# Below lists detail all eight possible movements
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# check if it is possible to go to pixel (x, y) from the current pixel.
# The function returns false if the pixel has a different color, or it's not a valid pixel
def safe_or_not(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target


def floodfill(twodarr, start_x, start_y, target_color, replacement_color):
    solution = {}

    # Change color of target index
    # Check if surrounding indices same color and reachable from target
    if len(twodarr) != 0 and twodarr[start_x][start_y] == target_color:

        # create a queue and enqueue starting pixel
        q = deque()
        twodarr[start_x][start_y] = replacement_color
        solution[start_x, start_y] = 1
        q.append((start_x, start_y))

        # break when the queue becomes empty
        while q:

            # dequeue front node and process it
            x, y = q.popleft()
            solution[x, y] = 1

            # process all eight adjacent pixels of the current pixel and
            # enqueue each valid pixel
            for k in range(len(row)):
                # if the adjacent pixel at position (x + row[k], y + col[k]) is
                # is valid and has the same color as the current pixel
                if safe_or_not(twodarr, x + row[k], y + col[k], target_color):
                    # replace the current pixel color with that of replacement
                    twodarr[x + row[k]][y + col[k]] = replacement_color

                    # enqueue adjacent pixel
                    q.append((x + row[k], y + col[k]))

    Answer_P(solution)


def main():
    # read in test files here then run them
    exec(open('testcase-1.py').read())
    exec(open('testcase-2.py').read())
    exec(open('testcase-3.py').read())
    exec(open('testcase-4.py').read())
    exec(open('testcase-5.py').read())



if __name__ == "__main__":
    main()
