import sys
sys.setrecursionlimit(10**6)
def preorder(arrX, arrY, ans):
    root = arrY[0]
    idx = arrX.index(root)
    arr_left = []
    arr_right = []
    for i in range(1, len(arrY)):
        if root[0] > arrY[i][0]:
            arr_left.append(arrY[i])
        else:
            arr_right.append(arrY[i])
    ans.append(root[2])
    if len(arr_left) > 0:
        preorder(arrX[:idx], arr_left, ans)
    if len(arr_right) > 0:
        preorder(arrX[idx+1:], arr_right, ans)
    return 
    
def postorder(arrX, arrY, ans):
    root = arrY[0]
    idx = arrX.index(root)
    arr_left = []
    arr_right = []
    for i in range(1, len(arrY)):
        if root[0] > arrY[i][0]:
            arr_left.append(arrY[i])
        else:
            arr_right.append(arrY[i])
    
    if len(arr_left) > 0:
        postorder(arrX[:idx], arr_left, ans)
    if len(arr_right) > 0:
        postorder(arrX[idx+1:], arr_right, ans)
    ans.append(root[2])
    return 
    
def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    sortedY = sorted(nodeinfo, key = lambda x: (-x[1], x[0]))
    sortedX = sorted(nodeinfo)
    
    preorder_list = []
    preorder(sortedX, sortedY, preorder_list)
    postorder_list = []
    postorder(sortedX, sortedY, postorder_list)

    return [preorder_list, postorder_list]