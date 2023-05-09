n = int(input())

matrix = [[0 for x in range(n)] for y in range(n)]

x, y = 0, 0
num = 1
down, right = True, False

while num <= n*n:
    matrix[y][x] = num
    num += 1
    
    if down:
        if y == n-1:
            down = False
            right = True
            x += 1
        elif x == 0:
            down = False
            right = True
            y += 1
        else:
            y += 1
            x -= 1
    elif right:
        if x == n-1:
            down = True
            right = False
            y += 1
        elif y == 0:
            down = True
            right = False
            x += 1
        else:
            x += 1
            y -= 1

for i in range(n):
    for j in range(n):
        if(j==n-1):
            print(matrix[i][j],"u")
        else:
            print(matrix[i][j], end=" ")
