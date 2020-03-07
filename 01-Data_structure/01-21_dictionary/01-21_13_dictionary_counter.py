# -*- coding: utf-8 -*- 

from collections import Counter

def counter_ex():
    seq1=[1,2,3,5,1,2,5,5,2,5,1,4]
    seq_counts = Counter(seq1)
    print(seq_counts)

    seq2=[1,2,3]
    seq_counts.update(seq2)
    
    seq3= [1,4,3]
    for key in seq3:
        seq_counts[key] +=1
    seq_counts_2 = Counter(seq3)
    print(seq_counts)

counter_ex