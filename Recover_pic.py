class Node:
    def __init__(self,val,isLeaf,scope,topL,topR,bottomL,bottomR):
        self.val = val
        self.isLeaf = isLeaf
        self.scope = scope
        self.topL = topL
        self.topR = topR
        self.bottomL = bottomL
        self.bottomR = bottomR

def construct(x1,x2,y1,y2):
    val = readSource(x1,y1,x2,y2)
    if val == 0:
        root = Node(-1,False,(x1,x2,y1,y2),None,None,None,None)
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        topL = construct(x1,mid_x,y1,mid_y)
        topR = construct(x1,mid_x,mid_y + 1,y2)
        bottomL = construct(mid_x + 1,x2,y1,mid_y)
        bottomR = construct(midx_x + 1,x2,mid_y + 1,y2)
        root.topL = topL
        root.topR = topR
        root.bottomL = bottomL
        root.bottomR = bottomR
        return root
    else:
        root = Node(val,True,(x1,x2,y1,y2),None,None,None,None)
        return root

def draw(node):
    if node.isLeaf:
        if node.val == 1:
            x1,x2,y1,y2 = node.scope
            writeTarget(x1,y1,x2,y2)
    else:
        draw(node.topL)
        draw(node.topR)
        draw(node.bottomL)
        draw(node.bottomR)

def main(x1,x2,y1,y2):
    root = construct(x1,x2,y1,y2)
    draw(root)




    