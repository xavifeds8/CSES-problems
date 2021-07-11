n = int(input())
lst = []
grid=[]
for i in range(n):
    x = input()
    for j in x:
        if j==".":
            lst.append(0)
        else:
            lst.append(-1)
    grid.append(lst)
    lst = []


if grid[n-1][n-1] == -1:

    print(0)
else:
    grid[n-1][n-1] = 1
    for i in range(n-2 , -1 , -1):
        if grid[n-1][i] == -1 or grid[n-1][i+1]==0:

            grid[n-1][i] = 0
        else:
            grid[n-1][i] = 1
        
    for i in range(n-2 , -1 , -1):
        if grid[i][n-1] == -1 or grid[i+1][n-1]==0:
            grid[i][n-1] = 0
        else:grid[i][n-1] = 1
        

    for i in range(n-2 , -1 , -1):
        for j in range(n-2 , -1, -1):
            if grid[i][j] == -1:
                grid[i][j] = 0
                continue
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
    print(grid[0][0]%(1000000007))


        
        
    

