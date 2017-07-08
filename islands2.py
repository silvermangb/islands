import random


def display_map(p_m):
    for row in p_m:
        x = ['% 3d' % i for i in row]
        print x


def traverse(p_map, p_rows, p_cols, p_island_color, p_islands):
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
            centroid_data = [0, 0, 0, 0]
            while stack:
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

                centroid_data[0] += top[0]
                centroid_data[1] += 1
                centroid_data[2] += top[1]
                centroid_data[3] += 1
                stack.pop()

            if centroid_data[1] > 0 or centroid_data[3] > 0:
                r_cent = 0
                if centroid_data[1] > 0:
                    r_cent = float(centroid_data[0]) / centroid_data[1]
                c_cent = 0
                if centroid_data[3] > 0:
                    c_cent = float(centroid_data[2]) / centroid_data[3]
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


data2(rows, cols, input_data, 1)

print 'input'
display_map(input_data)
islands = []
traverse(input_data, rows, cols, 1, islands)
print 'output'
display_map(input_data)

print len(islands)
for i in islands:
    print i
