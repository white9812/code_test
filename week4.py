n,m=map(int,input().split())
squares=[list(map(int,input()))for _ in range(n)]
quadrate=[]
for k in range(n):
    for i in range(n):
        for j in range(m):
            for h in range(m):
               
                        if squares[i][j]==squares[i][h]==squares[k][j]==squares[k][h] and abs(i-k) ==abs(h-j):
                            quadrate.append(h-j)
                            
print(max(quadrate)+1)