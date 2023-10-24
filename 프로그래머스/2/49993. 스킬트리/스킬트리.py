def solution(skill, skill_trees):
    ans = 0
    for s in skill_trees:
        skill_seq = list(skill).copy(); key = False
        for i in s:
            if i in skill_seq:
                if skill_seq.index(i) != 0:
                    key = True
                    break
                else:
                    skill_seq.remove(i)
        if not key:
            ans +=1
    return ans