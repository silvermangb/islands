import random


def display_map(p_m):
    for row in p_m:
        x = ['% 3d' % i for i in row]
        print x


def traverse(p_map, p_rows, p_cols, p_island_color, p_islands):
    row_i = 0
    col_i = 1
    size_i = 2

    loc = [-1, -1]

    stack = []

    while loc[row_i] + 1 < p_rows:

        loc[row_i] += 1
        loc[col_i] = -1
        while loc[col_i] + 1 < p_cols:
            loc[col_i] += 1
            if p_map[loc[row_i]][loc[col_i]] > 1:
                continue
            stack.append((loc[row_i], loc[col_i], p_island_color))
            size = 0
            row_sum = 0
            col_sum = 0
            while stack:
                top = stack[-1]
                if p_map[top[row_i]][top[col_i]] == 0:
                    stack.pop()
                    continue
                elif p_map[top[row_i]][top[col_i]] == 1:
                    p_island_color += 1
                    p_map[top[row_i]][top[col_i]] = p_island_color
                if top[row_i] - 1 > -1:
                    if p_map[top[row_i] - 1][top[col_i]] == 1:
                        p_map[top[row_i] - 1][top[col_i]] = p_map[top[row_i]][top[col_i]]
                        stack.append((top[row_i] - 1, top[col_i], p_map[top[row_i]][top[col_i]]))
                        continue
                if top[row_i] + 1 < p_rows:
                    if p_map[top[row_i] + 1][top[col_i]] == 1:
                        p_map[top[row_i] + 1][top[col_i]] = p_map[top[row_i]][top[col_i]]
                        stack.append((top[row_i] + 1, top[col_i], p_map[top[row_i]][top[col_i]]))
                        continue
                if top[col_i] - 1 > -1:
                    if p_map[top[row_i]][top[col_i] - 1] == 1:
                        p_map[top[row_i]][top[col_i] - 1] = p_map[top[row_i]][top[col_i]]
                        stack.append((top[row_i], top[col_i] - 1, p_map[top[row_i]][top[col_i]]))
                        continue
                if top[col_i] + 1 < p_cols:
                    if p_map[top[row_i]][top[col_i] + 1] == 1:
                        p_map[top[row_i]][top[col_i] + 1] = p_map[top[row_i]][top[col_i]]
                        stack.append((top[row_i], top[col_i] + 1, p_map[top[row_i]][top[col_i]]))
                        continue

                size += 1
                row_sum += top[row_i]
                col_sum += top[col_i]


                stack.pop()

            if size > 0:
                r_cent = float(row_sum) / size
                c_cent = float(col_sum) / size
                p_islands.append((p_island_color, r_cent, c_cent))


rows = 16
cols = 16
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


data2(rows, cols, input_data, .5)

print 'input'
display_map(input_data)
islands = []
traverse(input_data, rows, cols, 1, islands)
print 'output'
display_map(input_data)

print len(islands)
for i in islands:
    print i
