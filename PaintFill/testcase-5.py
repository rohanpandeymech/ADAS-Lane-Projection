from PaintFill import floodfill

mat = [
    ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R'],
    ['B', 'B', 'B', 'B', 'R', 'R', 'X', 'X'],
    ['R', 'R', 'R', 'R', 'R', 'R', 'X', 'X'],
    ['Y', 'Y', 'Y', 'Y', 'R', 'R', 'R', 'X'],
    ['Y', 'G', 'X', 'X', 'X', 'X', 'X', 'X']
]

# start node
x = 2
y = 6
replacement = 'g'

# replace the target color with a replacement color
floodfill(mat, x, y, 'X',replacement)