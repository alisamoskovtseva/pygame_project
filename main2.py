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
print(sud)
# [[7, 9, 5, 8, 0, 2, 1, 6, 4],
#  [8, 4, 3, 6, 5, 7, 2, 9, 0],
#  [6, 2, 0, 1, 9, 3, 7, 5, 8],
#  [2, 3, 8, 4, 6, 0, 9, 1, 7],
#  # [5, 6, 1, 7, 3, 9, 8, 2, 0],
#  [9, 0, 4, 5, 2, 1, 6, 3, 0],
#  [0, 1, 2, 3, 7, 6, 4, 8, 5],
#  [4, 7, 9, 0, 8, 5, 3, 0, 2],
#  [3, 5, 6, 9, 1, 4, 0, 7, 0]]
