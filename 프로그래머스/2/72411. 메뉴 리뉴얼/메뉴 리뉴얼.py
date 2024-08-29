from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        new_course = []
        for order in orders:
            lst = combinations(sorted(order), c)
            new_course += lst
        counter = Counter(new_course)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    answer.sort()
    return answer