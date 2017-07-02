import pprint

'''
000000
011110
011110
011110
000000
'''


def traverse(p_map, p_rows, p_cols, p_island_color, ):
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


rows = 8
cols = 8
input_data = [[0 for j in xrange(cols)] for i in xrange(rows)]

input_data[0] = [1 for i in xrange(cols)]
input_data[rows - 1] = [1 for i in xrange(cols)]
for i in xrange(rows):
    input_data[i][0] = 1
    input_data[i][cols - 1] = 1

for r in xrange(3, 6):
    for c in xrange(3, 6):
        input_data[r][c] = 1
input_data[2][2] = 1

pprint.pprint(input_data)

island_color = 1

island_count = traverse(input_data, rows, cols, 1) - 1

for row in input_data:
    row = ['%02d' % i for i in row]
    print str(row)
print island_count
