def dfs(x1,x2,y1,y2):
    val = readSource(x1,y1,x2,y2)
    if val == 1:
        writeTarget(x1,y1,x2,y2)
    elif val == 0:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        dfs(x1,mid_x,y1,mid_y)
        dfs(x1,mid_x,mid_y + 1,y2)
        dfs(mid_x + 1,x2,y1,mid_y)
        dfs(mid_x + 1,x2,mid_y + 1,y2)