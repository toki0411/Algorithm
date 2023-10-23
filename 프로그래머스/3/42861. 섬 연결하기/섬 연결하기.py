def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x==y:return  #두 노드는 이미 연결되어있음(부모가 같기 때문)
    parent[x] = y
    
def find(parent, x):
    if parent[x] == x : return x  #자기 자신을 부모로 가지면 리턴 
    parent[x] = find(parent, parent[x]) # 부모를 찾기 위해 재귀적으로 실행
    return parent[x]
    
def solution(n, costs):
    answer = cnt = 0
    parent = [i for i in range(n)]
    #간선 비용 적은 순 정렬 
    costs.sort(key = lambda x: x[2])
    #유니온 파인드를 이용하여 섬들을 연결 
    for i in range(len(costs)):
        if find(parent, costs[i][0]) != find(parent, costs[i][1]):  # 비용 적은 순으로, 두 섬이 연결되어 있는지 체크 (부모를 체크해서 다르면 연결x)
            union(parent, costs[i][0], costs[i][1])  # 두 섬을 연결
            answer += costs[i][2] # 비용 추가 
            cnt +=1 
        if cnt == n : break
    return answer