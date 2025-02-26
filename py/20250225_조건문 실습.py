# 조건문 활용하기
# 문제1 - 사용자로부터 두개의ㅏ 값을 입력을 받는다. 첫번째 값이 크다면 "win", 두번째 값이 크다면"lose"를 출력하라
# 내가 한것 
# value1 = input(int)
# value2 = input(int)

# if value1> value2 :
#     print("win")
# else:
#     print("losd")

# 답
# 사용자로부터 두개의 값을 입력 받는다.
# var1 = input("첫번째 값을 입력해주세요:")
# var2 = input("두번째 값을 입력해주세요:")

# 입력밧을 숫자로 변환
# num_var1 = int(var1) # 값은 정수형 데이터 타입으로 변환하게 됨
# num_var2 = int(var2)

# if num_var1 > num_var2:
#     print("win")
# elif num_var1 < num_var2:
#     print("lose")
# else:
#     print("draw")

#문제2 - 시험 점수를 입력 받는다. 점수는 1-99점이다.(이외의 값이 들어오면 프로그램을 종료한다.)/ A: 90-99,B: 80-89,C: 70-79,D:60-69,F:-59/ 시험 점수에 맞는 성적을 출력한다. 
# 내가
score = input("시험 점수를 입력하시오")

score_num = int(score)

if 90 <= score_num <=99:
    print("A")
elif 80 <= score_num <= 89:
    print("B")
elif 70 <= score_num <= 79:
    print("C")
elif 60 <= score_num <= 69:
    print("D")
elif score_num <= 59:
    print("F")
else:
    print("잘못된 값입니다. 종료합니다.")
    exit()

# 정답
score = int(input("Enter the score: "))

if score <= 99 and score >= 90:  # A
    grade = "A"
elif score <= 89 and score >= 80:  # B
    grade = "B"
elif score <= 79 and score >= 70:  # C
    grade = "C"
elif score <= 69 and score >= 60:  # D
    grade = "D"
elif score <= 59 and score >= 1:  # F
    grade = "F"
else:
    grade = None

if grade is not None:
    print(f"등급은 {grade}입니다.")