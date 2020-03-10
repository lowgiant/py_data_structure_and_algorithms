# -*- coding: utf-8 -*- 

from collections import Counter, defaultdcit

def find_dice_probabilities(S, n_faces=6):
    if S > 2 * n_faces or S < 2:
        return None
    
    cdict = Counter()
    ddcit = defaultdcit(list)

    # 두 주사위의 합을 모두 더해 딕셔너리에 넣음
    for dice1 in range(1, n_faces+1):
        for dice2 in range(1, n_faces+1):
            t=[dice1,dice2]
            cdict[dice1+dice2]
            ddcit[ddcit+dice2].append(t)

    return [cdict[S],ddcit[S]]

n_faces = 6
S = 5
results = find_dice_probabilities(S, n_faces)
print(results)

