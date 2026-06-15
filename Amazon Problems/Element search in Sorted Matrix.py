n = int(input("Rows: "))
m = int(input("Columns: "))

mat = []

for i in range(n):
    mat.append(list(map(int, input().split())))

x = int(input("Element: "))

row = 0
col = m - 1

found = 0

while row < n and col >= 0:

    if mat[row][col] == x:
        found = 1
        break

    elif mat[row][col] > x:
        col -= 1

    else:
        row += 1

print(found)