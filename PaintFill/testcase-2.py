# Average array test case

from PaintFill import floodfill

mat = [
    ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
    ['R', 'R', 'R', 'R', 'R', 'R', 'X', 'X', 'X'],
    ['Y', 'Y', 'Y', 'Y', 'R', 'R', 'R', 'X', 'X'],
    ['Y', 'G', 'G', 'G', 'G', 'R', 'X', 'X', 'X'],
    ['Y', 'G', 'G', 'G', 'R', 'R', 'X', 'X', 'X'],
    ['Y', 'G', 'X', 'G', 'G', 'G', 'G', 'X', 'X'],
    ['Y', 'G', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

# start node
x = 0
y = 0
replacement = 'X'

# replace the target color with a replacement color
floodfill(mat, x, y, 'B',replacement)
