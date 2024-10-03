import heapq

def solution(genres, plays):
    answer = []
    dic = {}
    genre_cnt = []
    
    for i, genre in enumerate(genres):
        if genre not in dic:
            dic[genre] = [(plays[i], i)]
        else:
            dic[genre].append((plays[i], i))
    
    for genre in dic:
        genre_plays = sum([play for play, _ in dic[genre]])
        heapq.heappush(genre_cnt, (-genre_plays, genre))  
        
    while genre_cnt:
        _, genre = heapq.heappop(genre_cnt)
        musics = dic[genre]
        musics.sort(key=lambda x: (-x[0], x[1]))
        answer.append(musics[0][1])
        if len(musics) > 1:
            answer.append(musics[1][1])
    
    return answer