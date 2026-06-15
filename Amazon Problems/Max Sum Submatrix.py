def kadane(arr):

    current = arr[0]
    best = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        best = max(best, current)

    return best


r = int(input("Rows: "))
c = int(input("Columns: "))

mat = []

for i in range(r):
    mat.append(list(map(int, input().split())))

result = float('-inf')

for left in range(c):

    temp = [0] * r

    for right in range(left, c):

        for row in range(r):
            temp[row] += mat[row][right]

        result = max(result, kadane(temp))

print(result)