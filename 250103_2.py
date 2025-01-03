# 조합 예시
# 샴 네트워크: 투이미지를 받아서 같은지 다른지 판단하는 방식으로 동작하는 네트워크 => 두개의 이미지의 순서는 바뀌어도 상관이 없다는 점  

## 파이썬을 이용한 조합 계산

from itertools import combinations

arr =['a','b','c']
# 원소 중에서 2개를 뽑는 모든 조합 계산
result = list(combinations(arr,2))
print(result)

# 중복 순열 
# 서로 다른 n개에서 중복을 포함해 r개를 뽑아 특정한 순서로 나열하는 것을 의미한다.

## 파이썬을 이용한 중복 순열 계산

from itertools import product

arr2 =['a','b','c']
# 원소 중에서 2개를 뽑는 모든 중복 순열 계산
result2 = list(product(arr2,repeat=2))
print(result2)

# product: 데카르트 곱(cartesian product)을 구하는 함수로, 중복을 허용한 순열을 생성합니다.
# product(arr2, repeat=2):
# arr2에서 2개의 원소를 뽑아 중복을 허용해 모든 가능한 조합을 생성합니다.
# 중복을 허용하기 때문에, 같은 요소가 반복해 나올 수 있습니다.
# repeat=2는 두 번 선택하는 것을 의미합니다.

# 중복 조합 : 서로 다른 n개에서 중복을 포함해 순서를 고려하지 않고 r개를 뽑는 것을 의미  
# 중복 조합 예시 
# 딥러닝에서 학습된 모델의 결과를 활용하여 최종적인 결과를 생성하는 앙상블 방법이 존재 

from itertools import combinations_with_replacement

arr3 = ['a','b','c']
# 원소 중에서 2개를 뽑는 모든 중복 조합 계산
result3 = list(combinations_with_replacement(arr3,2))
print(result3)