n = int(input("Size: "))

arr = list(map(int, input("Elements: ").split()))

key = int(input("Key: "))

low = 0
high = n - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == key:
        print(mid)
        break

    if arr[low] <= arr[mid]:

        if arr[low] <= key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    else:

        if arr[mid] < key <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1

else:
    print(-1)