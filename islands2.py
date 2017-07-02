import random
'''
000000
011110
011110
011110
000000
'''

max_stack = 0

def traverse(p_map, p_rows, p_cols, p_island_color, ):
    global max_stack

    loc = [-1, -1]

    stack = []

    while loc[0] + 1 < p_rows:

        loc[0] += 1
        loc[1] = -1
        while loc[1] + 1 < p_cols:
            loc[1] += 1
            if p_map[loc[0]][loc[1]] > 1:
                continue
            stack.append((loc[0], loc[1], p_island_color))
            while stack:
                if len(stack) > max_stack:
                    max_stack = len(stack)
                top = stack[-1]
                if p_map[top[0]][top[1]] == 0:
                    stack.pop()
                    continue
                elif p_map[top[0]][top[1]] == 1:
                    p_island_color += 1
                    p_map[top[0]][top[1]] = p_island_color
                if top[0] - 1 > -1:
                    if p_map[top[0] - 1][top[1]] == 1:
                        p_map[top[0] - 1][top[1]] = p_map[top[0]][top[1]]
                        stack.append((top[0] - 1, top[1], p_map[top[0]][top[1]]))
                        continue
                if top[0] + 1 < p_rows:
                    if p_map[top[0] + 1][top[1]] == 1:
                        p_map[top[0] + 1][top[1]] = p_map[top[0]][top[1]]
                        stack.append((top[0] + 1, top[1], p_map[top[0]][top[1]]))
                        continue
                if top[1] - 1 > -1:
                    if p_map[top[0]][top[1] - 1] == 1:
                        p_map[top[0]][top[1] - 1] = p_map[top[0]][top[1]]
                        stack.append((top[0], top[1] - 1, p_map[top[0]][top[1]]))
                        continue
                if top[1] + 1 < p_cols:
                    if p_map[top[0]][top[1] + 1] == 1:
                        p_map[top[0]][top[1] + 1] = p_map[top[0]][top[1]]
                        stack.append((top[0], top[1] + 1, p_map[top[0]][top[1]]))
                        continue
                stack.pop()
    return p_island_color


rows = 1024
cols = 1024
input_data = [[0 for j in xrange(cols)] for i in xrange(rows)]


def data1(p_rows, p_cols, p_input_data):
    p_input_data[0] = [1 for i in xrange(p_cols)]
    p_input_data[rows - 1] = [1 for i in xrange(p_cols)]
    for i in xrange(p_rows):
        p_input_data[i][0] = 1
        p_input_data[i][p_cols - 1] = 1

    for r in xrange(3, 6):
        for c in xrange(3, 6):
            p_input_data[r][c] = 1
    p_input_data[2][2] = 1


def data2(p_rows, p_cols, p_input_data, p_percent):
    cell_count = p_rows * p_cols
    ones = int(p_percent * cell_count)
    cells = [(i, j) for j in xrange(p_cols) for i in xrange(p_rows)]
    land_cells = random.sample(cells, ones)
    for p in land_cells:
        p_input_data[p[0]][p[1]] = 1


data2(rows, cols, input_data, .75)


island_count = traverse(input_data, rows, cols, 1) - 1

print island_count
print max_stack
