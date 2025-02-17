# 빈 튜플 생성
tuple = (1,) # 하나의 값을 넣어도 콤마를 뒤에 붙여서 이 값은 튜플을 위한 것이다라는걸 알려줘야함
# 튜플은 불변속성을 가지고 있기 때문에 이미 생성된 튜플에 어떤 값을 추가해주는 append 사용 불가능

# 과일 바구니 
fruits = ()




# 튜플 언패킹
values = (1,2,3,6,4,5)
val1,*vals,val2,val3 = values
print(vals)
 # 왜 vals 값이 [2,3] 임? 맨 첫번째 요소와, 뒤에서 두번째 선언하는 것 말고 , 중간 값들이 리스트 형태로 저장

# 튜플 패킹 언패팅의 값 교환
a = 10
b = 20

# 서로의 값을 교환 하고 싶다면?
# 원본
# temp = a # a = 10,b = 20, temp = 10
# a = b # a = 20, b= 20, temp = 10
# b = temp  # a = 20 , b= 10, temp = 10
# 패킹, 언패킹
a,b = b,a # (20,10)
print("a:",a)

tp = (1,2,3,4,5,6,7,8)
val1,val2,val3,*vals,_ =tp
vals.append(10)
print(vals)