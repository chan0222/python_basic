# 셋 정의 // 셋 정의한다고 {} 사용하면 딕셔너리도 인식함
empty_set = set()
my_set = {1,2,3,3} # 특정값을 중복해서 한다면 중복된 값은 버려지고 유니크 한 값만 셋에 저장됨

# fruits = {"apple","banana","blueberry"}
# print(fruits)

# fruits.add("orange")
# print(fruits) # 셋은 요소들의 순서를 보장하지 않음

# fruits.remove("banana")
# print(fruits)

fruits1 = {"apple","strawberry","peach"}
fruits2={"banana","strawberry","orange"}

#합집합
union =fruits1.union(fruits2)
print(union)
print(fruits1|fruits2)
#교집합
intersection = fruits1.intersection(fruits2)
print(intersection)
print(fruits1&fruits2)
#차집합 // 순서가 중요함
diff1 =fruits1.difference(fruits2)
diff2 =fruits2.difference(fruits1)
print("차집합 f1-f2",diff1)
print("차집합 f2-f1",diff2)
