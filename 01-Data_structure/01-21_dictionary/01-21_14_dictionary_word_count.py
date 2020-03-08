# -*- coding: utf-8 -*- 

from collections import Counter

def find_top_N_recurring_words(seq, N):
    dcounter =Counter()
    for word in seq.split():
        dcounter[word] +=1
    return dcounter.most_common(N)

seq = "워드 카운터 얼마나 성능이 좋은지 확인 해볼까? 워드 몇번이냐? 성능 어때? 워드 이렇게 나오군ㅋㅋ"
N = 3

func = find_top_N_recurring_words(seq,N)

print("워드당 갯수를 세워주는 함수:",func)