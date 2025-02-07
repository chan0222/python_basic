# while 문은 조건문이 참인 동안 while 문에 속한 문장들이 반복해서 수행된다. 
# 열번 찍어 안 넘어가는 나무 없다
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")

# %d 정수(int)를 삽입하는 자리 표시자 
# %f 실수(float)
#%.2f 소수점 두번째 자리 까지 
# %s 문자열 

# 와일문 만들기
## 여러가지 선택지 중 하나를 선택해서 입력받은 예제 
# 모르겟
# prompt = """
# ... 1. Add
# ... 2. Del
# ... 3. List
# ... 4. Quit
# ...
# ... Enter number: """
# number = 0
# while number != 4:
#      print(prompt)
# number = int(input())


# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number:

#while 문 강제로 빠져나가기 
# coffee.py
coffee = 10 
while True:
    money = int(input("돈을 넣어주세요:")) #사용자로부터 값을 입력받는 부분이고 입력받은 숫자를 money 변수에 대입하는 것
    if money == 300 :
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커필ㄹ 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# while 문의 맨처음 으로 돌아가기
# continue문 while 문을 빠져나가지 않고 while 문의 맨처음(조건문)으로 다시 돌아가게 만들고 싶은 경우
## 1부터 10/가지의 숫자 중에서 홀수만 출력하는 것을 while문을 사용해서 작성한다고 하면?
a = 0 
while a < 10:
    print()