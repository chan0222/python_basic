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
