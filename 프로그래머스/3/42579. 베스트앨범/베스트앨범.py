def solution(genres, plays):
    dict = {}; genre_play = {}; ans = []
    for i in range(len(genres)):
        gen = genres[i]; play = plays[i]
        if gen in dict:
            dict[gen].append([i, play])
            genre_play[gen] += play
        else:
            dict[gen] = []
            dict[gen].append([i,play])
            genre_play[gen] = play

    genre_times = sorted(genre_play.items(), reverse = True, key = lambda x: x[1])
    for i in genre_times:
        genre_play_time = sorted(dict[i[0]], reverse= True,key = lambda x:x[1] )   
        if len(genre_play_time) < 2:
            ans.append(genre_play_time[0][0])
        else:
            for j in range(2):
                ans.append(genre_play_time[j][0])       
    return ans