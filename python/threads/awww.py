a = [0] * 8
arr = []
for _ in range(8):
    arr.append(a)


for i in range(8):
    for j in range(8):
        arr[i][j] = i*j

for i in range(8):
    print(arr[i])
