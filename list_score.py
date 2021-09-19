a = int(input())
c = []
count = 0
for i in range(a) :
    b = list(map(int,input().split(" ")))
    c.append(b)

for i in range(a) :
    d = sum(c[i]) - (c[i][0])
    d = d / c[i][0]

    for j in range(1, c[i][0]+1) :
        if c[i][j] > d :
            count = count + 1
    print("%.3f%%"%((100/c[i][0]) * count))
    count = 0
