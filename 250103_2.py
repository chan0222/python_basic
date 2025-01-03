## 파이썬을 이용한 조합 계산

from itertools import combinations

arr =['a','b','c']
# 원소 중에서 2개를 뽑는 모든 조합 계산
result = list(combinations(arr,2))
print(result)