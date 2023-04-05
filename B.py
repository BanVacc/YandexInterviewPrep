n = int(input())
vec = []

# Заполнение вектора
for i in range(n):
    vec.append(int(input()))

max = 0

now = 0
for s in vec:
    if s == 1:
        now += 1
    else:
        now = 0
        
    if now > max:
        max = now
    

print(max)
