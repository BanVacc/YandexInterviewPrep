gems = list(input())
st = input()

ans = 0
for s in st:
    if s in gems:
        ans += 1

print(ans)