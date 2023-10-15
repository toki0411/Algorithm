from itertools import permutations
def check(user, banned_id):
    for i in range(len(banned_id)):
        if len(user[i]) == len(banned_id[i]):
            for j in range(len(banned_id[i])):
                if banned_id[i][j] == '*':
                    continue
                elif banned_id[i][j] != user[i][j]:
                    return False
        else:
            return False
    return True
def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []
    for user in user_permutation:
        if check(user, banned_id):
            user = set(user)
            if user not in ban_set:
                ban_set.append(user)

    return len(ban_set)