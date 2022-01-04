import random

# inputarr = input().split()
st = '1 5 8 6 3 2 8 9 0 4'
# inputarr = map(int, st.split())
# print(inputarr)
# arr = list(filter(lambda x: x % 2 == 0, inputarr))

# print(arr)
# print(len(arr))

# print(arr[random.randint(0, len(arr) - 1)])

print(' '.join(sorted(list(map(int, st.split())), reverse=True)))