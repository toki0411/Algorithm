import heapq
T = int(input())
for t in range(T):
    pq = [] #오름차순 정렬
    pq_reverse = [] #내림차순 정렬
    numDict = dict()
    k = int(input())
    for i in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
                heapq.heappush(pq, num)
                heapq.heappush(pq_reverse, -num)
        elif cmd == 'D':
            if num == -1 and len(pq) > 0:  #최소값 삭제
                while len(pq) > 0:
                    tmp = heapq.heappop(pq)
                    if tmp in numDict and numDict[tmp] > 0:
                        numDict[tmp] -= 1
                        if numDict[tmp] == 0:
                            del numDict[tmp]
                        else:
                            heapq.heappush(pq, tmp)
                        break
            elif num == 1 and len(pq_reverse) > 0 :  #num == 1, 최대값 삭제
                while len(pq_reverse) > 0:
                    tmp = heapq.heappop(pq_reverse)
                    if -tmp in numDict and numDict[-tmp] > 0 :
                        numDict[-tmp] -= 1
                        if numDict[-tmp] == 0:
                            del numDict[-tmp]
                        else:
                            heapq.heappush(pq_reverse, tmp)
                        break
        # print(pq, pq_reverse, numDict)
    ansList = numDict.items()
    ansList = list(ansList)
    # print(ansList)
    if len(ansList) == 0:
        print("EMPTY")
    else:
        ansList.sort(key = lambda x: x[0])
        print(ansList[-1][0], ansList[0][0])