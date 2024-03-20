field = [list('-' * 10)]
for i in range(8):
    field.append(['-'] + list(input()) + ['-'])
field.append(list('-' * 10))
for i in range(1, 10):
    for j in range(1, 10):
        if field[i][j] == 'R' or field[i][j] == 'B':
            if field[i][j] == 'R':
                di = [0, 0, 1, -1]
                dj = [1, -1, 0, 0]
            else:
                di = [1, 1, -1, -1]
                dj = [1, -1, 1, -1]
            for dest in range(4):
                ni, nj = i + di[dest], j + dj[dest]
                while field[ni][nj] == '*' or field[ni][nj] == '.':
                    field[ni][nj] = '.'
                    ni += di[dest]
                    nj += dj[dest]
ans = 0
for row in field:
    for cell in row:
        if cell == '*':
            ans += 1
print(ans) 