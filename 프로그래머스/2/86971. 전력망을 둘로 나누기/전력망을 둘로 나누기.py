def findParents(x):
    global parents
    if x == parents[x]:
        return x
    parents[x] = findParents(parents[x])
    return parents[x]

def union(a, b):
    global parents
    aRoot = findParents(a)
    bRoot = findParents(b)
    if aRoot < bRoot:
        parents[bRoot] = aRoot
    else:
        parents[aRoot] = bRoot
        
def solution(n, wires):
    wires.sort()
    global parents
    answer = 1e9
    for i in range(n-1):
        parents = [i for i in range(n+1)]
        for j in range(n-1):
            if i != j:
                a, b = wires[j][0], wires[j][1]
                union(a,b)
  
        
        diff = {}
        for i in range(1, n+1):
            p = findParents(parents[i])
            if p in diff:
                diff[p] += 1
            else:
                diff[p] = 1
        diff = list(diff.values())
    
        if len(diff) == 2:
            answer = min(abs(diff[0]-diff[1]), answer)
    return answer