import random

hor = [set(range(1, 10)), set(range(1, 10)), set(range(1, 10)), set(range(1, 10)), set(range(1, 10)), set(range(1, 10)),
       set(range(1, 10)), set(range(1, 10)), set(range(1, 10))]
ver = [set(range(1, 10)), set(range(1, 10)), set(range(1, 10)), set(range(1, 10)), set(range(1, 10)), set(range(1, 10)),
       set(range(1, 10)), set(range(1, 10)), set(range(1, 10))]
kvadr = [[set(range(1, 10)), set(range(1, 10)), set(range(1, 10))],
         [set(range(1, 10)), set(range(1, 10)), set(range(1, 10))],
         [set(range(1, 10)), set(range(1, 10)), set(range(1, 10))]]

sud = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(9):
    for j in range(9):
        a = hor[i] & ver[j] & kvadr[i // 3][j // 3]
        a = list(a)
        if a:
            r = random.choice(a)
            sud[i][j] = r
            hor[i].remove(r)
            ver[j].remove(r)
            kvadr[i // 3][j // 3].remove(r)
print(*sud,sep='\n')
