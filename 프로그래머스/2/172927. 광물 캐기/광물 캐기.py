answer = 1e9
def dfs(dia, iron, stone, stemina, idx, minerals):
    global answer
    if idx == len(minerals) or (dia == 0 and iron == 0 and stone == 0):
        answer = min(stemina, answer)
        return 
    newIdx = idx + 5
    if newIdx > len(minerals):
        newIdx = len(minerals)
        
    if dia > 0:
        newStemina = calStemina(idx, newIdx, "dia", minerals)
        dfs(dia - 1, iron, stone, stemina + newStemina, newIdx, minerals)
    if iron > 0:
        newStemina = calStemina(idx, newIdx, "iron", minerals)
        dfs(dia, iron - 1, stone, stemina + newStemina, newIdx, minerals)
    if stone > 0:
        newStemina = calStemina(idx, newIdx, "stone", minerals)
        dfs(dia, iron, stone - 1, stemina + newStemina, newIdx, minerals)
                                
def calStemina(start, end, tool, minerals):
    stemina = 0;
    if tool == "dia":
        for i in range(start, end):
            stemina += 1
    elif tool == "iron":
         for i in range(start, end):
            if minerals[i] == "diamond":
                stemina += 5
            else:
                stemina += 1
    else:
        for i in range(start, end):
            if minerals[i] == "diamond":
                stemina += 25
            elif minerals[i] == "iron":
                stemina += 5
            else:
                stemina += 1       
    return stemina
                                
def solution(picks, minerals):
    dfs(picks[0], picks[1], picks[2], 0, 0, minerals)
    return answer