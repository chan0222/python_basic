from itertools import permutations

arr = [ 'a','b','c']

#원소 중에서 2개를 뽑는 모든 순열 계산 
result = list(permutations(arr,2))
print(result)
