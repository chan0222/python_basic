from itertools import permutations

arr = [ 'a','b','c']

#원소 중에서 2개를 뽑는 모든 순열 계산 
result = list(permutations(arr,2))
print(result)

# itertools: 파이썬에서 반복 가능한 데이터구조(리스트, 튜플 등)에서 조합, 순열 등 다양한 반복 작업을 쉽게 수행할 수 있도록 도와주는 표준 라이브러리 이다.
# permutations: itertools 에서 제공하는 함수로, 주어진 리스트 등에서 순열(순서가 다른 경우의 수)을 생성한다. 
# permutations(arr, 2):
# arr에서 2개의 원소를 선택해 나올 수 있는 모든 순열을 생성합니다.
# 순서가 다르면 다른 경우로 간주됩니다.

# list(): permutations는 이터레이터(iterator) 형태로 결과를 반환하기 때문에, 이를 보기 쉽게 리스트로 변환합니다.
# result에는 모든 경우의 수가 튜플 형태로 저장됩니다.

# 추가 설명 – 순열과 조합의 차이
# 순열 (Permutation): 순서가 중요 → ('a', 'b') ≠ ('b', 'a')
# 조합 (Combination): 순서가 중요하지 않음 → ('a', 'b') = ('b', 'a')