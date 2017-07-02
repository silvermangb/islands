import pprint

'''
000000
011110
011110
011110
000000
'''

max_depth = 0


def traverse(p_input_data, p_rows, p_cols, p_r, p_c, p_island_label, p_depth):
    global max_depth

    if p_depth > max_depth:
        max_depth = p_depth
    if p_r < 0 or p_r == p_rows:
        return
    elif p_c < 0 or p_c == p_cols:
        return

    if p_input_data[p_r][p_c] == 0:
        return
    if p_input_data[p_r][p_c] != 1:
        return

    p_input_data[p_r][p_c] = island_label

    if p_r >= 0:
        traverse(p_input_data, p_rows, p_cols, p_r - 1, p_c, p_island_label, p_depth + 1)
    if p_r <= p_rows - 1:
        traverse(p_input_data, p_rows, p_cols, p_r + 1, p_c, p_island_label, p_depth + 1)
    if p_c >= 0:
        traverse(p_input_data, p_rows, p_cols, p_r, p_c - 1, p_island_label, p_depth + 1)
    if c < p_cols:
        traverse(p_input_data, p_rows, p_cols, p_r, p_c + 1, p_island_label, p_depth + 1)


rows = 11
cols = 1
input_data = [[0 for j in xrange(cols)] for i in xrange(rows)]

c = 0
for row in xrange(rows):
    while c < cols:
        input_data[row][c] = 1
        c += 2
    c = c % cols

for r in xrange(rows):
    for c in xrange(cols):
        input_data[r][c] = 1

pprint.pprint(input_data)
island_label = 1

for r in xrange(rows):
    for c in xrange(cols):
        if input_data[r][c] == 1:
            island_label += 1
            traverse(input_data, rows, cols, r, c, island_label, 0)

island_count = island_label - 1

for row in input_data:
    row = ['%02d' % i for i in row]
    print str(row)
print island_count
print max_depth
