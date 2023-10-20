def solution(name):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    reverse_alphabet = alphabet[::-1]
    cnt = 0; size = len(name)
    min_move = len(name) - 1
    for idx, char in enumerate(name):
        # 현재 idx의 알파벳 변경하기
        cnt += min(alphabet.index(char), reverse_alphabet.index(char) + 1)
        # 커서 이동하기
        next_idx = idx + 1
        while next_idx < size and name[next_idx] == 'A' :
            next_idx += 1
        min_move = min([min_move, 2*idx + size - next_idx, idx + 2*(size - next_idx)])
    return cnt + min_move