n = int(input("Number of Pumps: "))

petrol = list(map(int, input("Petrol: ").split()))
distance = list(map(int, input("Distance: ").split()))

start = 0
balance = 0
deficit = 0

for i in range(n):

    balance += petrol[i] - distance[i]

    if balance < 0:
        start = i + 1
        deficit += balance
        balance = 0

if balance + deficit >= 0:
    print(start)
else:
    print(-1)