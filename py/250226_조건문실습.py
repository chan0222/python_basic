# # for loop
# for i in range(1,5): #range는 정해진 숫자 만큼의 값의 목록을 만들어주는 명령
#     print(i)
# else:
#     print("반복이 완료되었습니다. ")

# # while
# i = 0
# while i <5:
#     print(i)
#     i = i +1

# fruits = ["사과","딸기","복숭아","참외"]

# for fruit in fruits :
#     print(f"{fruit}이 과일 바구니에 있습니다.") 

# while True:
#     user_input =input("명령어를 입력해 주세요")
#     if user_input == "exit":
#          break
# else:
#       pass

# #구구단 프로그램
# #1~9단, n * 1 ~ n * 9
# for i in range(1,10):
#     for x in range(1,10):
#          print(f"{x} * {i} = {x * i}")

# # enumerate 활용하기

# fruits = ["apple","banana","blueberry","peach"]

# index = 1
# for fruit in fruits:
#      print(f"{index} 번째 과일은 {fruit} 입니다.")
#      index = index + 1

# # 언패킹

# for index,fruit in enumerate(fruits,start = 1):
#      print(f"{index} 번째 과일은 {fruit} 입니다.")
#      index = index + 1

# 팩토리얼 구하기 
# n! = n * (n-1)*...*2*1
num = 10
reseult = 1
for i in range(1,num +1):
     result = result * i
print(f"{num}! 은 {result} 입니다.")