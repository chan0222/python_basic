## 파이썬 2장 연습 문제
##1. 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동씨의 평균 점수를 구해보자 국어 80,영어 75 수학 55
a= {'국어':80,'영어':75,'수학':55}
b = a['국어'] + a['수학'] + a['영어']
c = b//len(a)
print(c)

##2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해보자
x = 13

if x % 2 == 1:
    print('홀수')
 
if x % 2 == 0:
    print('짝수')   

## 3. 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

# 슬라이싱 기법

d = "881120-1068234"

print(d[:6])
print(d[7:])

## 4.주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.

# 문자열 인덱싱 사용

pin = "881120-1068234"
print(pin[7])

## 5. 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.
e = "a:b:c:d"
f = e.replace(":","#")
print(f)

## 6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.

list = [1,3,5,4,2]
list.sort()
list.reverse()
print(list)

## 7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.

## 문자열의 join 함수?>
# 8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
