def deleteGreatestValue(grid):
    rows, cols = len(grid), len(grid[0]);
    res = 0;
    
    # this is ording the rows
    for x in range(rows):
        grid[x].sort();
        
    # going to the columns
    for j in range(cols):
        res += max(grid[i][j] for i in range(rows))
    return res;

   
print(deleteGreatestValue([[1,2,4],[3,3,1]]));