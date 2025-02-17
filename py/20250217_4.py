# 투루리스트를 어떻게 저장할 것인가?
# 여러개의 데이터를 저장하려면 리스트 튜플 딕셔너리 세트 >> 가벼운 데이터를 추가하고 삭제하기 때문에  튜플은 사용할수 없음 >> 리스트 또는 세트를 이용하는 것이 적당해 보임

todo_list = []

while True:
    print("")
    print("할 일 목록 관리자")
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 할 일 목록 보기")
    print("4. 종료")


    choice = input("선택:")

    if choice == "1":
        todo = input("추가할일:")
        todo_list.append(todo)
        print(f"{todo} 할일이 추가 되었습니다.")
    elif choice == "2":
        todo = input("삭제할 일:")
        todo_list.remove(todo)
        print(f"{todo} 할일이 삭제 되었습니다.")
    elif choice == "3":
        print(todo_list)
    elif choice == "4":
        break
    else:
        print("올바른 선택이 아닙니다. 다시 시도해보세요")