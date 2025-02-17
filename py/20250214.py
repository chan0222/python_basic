# my_list = [10,20,30]
# print(my_list)

# my_list =[30,40,50]
# my_list.append(10)
# my_list.append(15)
# my_list.append(20)

# print(my_list)

# sliced = my_list[3:] # 3번째 자리부터 끝까지 
# print("sliced:",sliced)

# 검색하기 좋은 리스트

# fruits = ["banana","apple","blueberry","cherry"]

# 바나나가 포함 되어있나요?
# is_banana_included = "banana" in fruits
# print("is banana included?", is_banana_included)

# 체리는 어디에 있나요?
# index_cherry =  fruits.index("cherry")
# print("cherry is ", index_cherry)

# 만약 리스트에 있는 값이 아니라 없는 값을 물어본다먼? 에러발생

# #리스트의 정렬
# numbers = [2,4,8,7,3,5,1,6]
# print("unsorted", numbers) #순서가 중요함

# numbers.sort()
# print("sorted", numbers)

# numbers.sort(reverse= True)
# print("sorted reverse", numbers)

# 리스트 연산 요소 추가 및 삭제 
list = []
list.append(10)
list.append(11)
list.append(12)
# print(list)

list.extend([13,14,15]) # 하나의 리스트의 요소로 들어감
# list.append([16,17]) # 리스트 형태로 요소로 들어감 // 복합 리스트의 형태로 들어감 넣은 값이 하나의 요소로
# print(list)

# print(list[-1]) # 리스트의 마지막 요소를 

# 리스트 연산
# new_list = list + [0,1,2]
# print(new_list)

# multi_list = [0,1,2] * 3
# print(multi_list)

# print(list)
# del list[0] # del 리스트 삭제하고자 하는 요소 자리
# print(list)

# 리스트를 활용한 최대값& 최소값 찾아오는 것
max_value = max(list)
min_value = min(list)
print(f"최대 값은 {max_value}, 최고 값은 {min_value} 입니다.")
