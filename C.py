n = int(input())

for i in range(n):
    new = input()

    if i == 0 or new != prev:
        print(new)

    prev = new