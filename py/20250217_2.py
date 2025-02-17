# 빈 딕셔너리
# dict = {}
# dict["key"] = "value"
# print(dict)

person = {"name": "홍길동","age": "30","city":"서울"}
person_detail = {"country" : "대한민국","married": True}
# 여러개의 딕셔너리 합성?
person.update(person_detail)

# 딕셔너리 값 추가 
# person["age"] = 35
# person["country"] ="대한민국"

# 이름 꺼내보기
# name = person["name"]
# print(name)
print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은{person['city']}입니다.")
# 키와 밸류를 의미있게 페어해서 코드를 작성 할수 있게 만들어주는게 딕셔너리

#만약 키에 지정되지 않은 값을 딕셔너리에 물어본다면 어떤 식의 문제가 발생? 에러가 남 그러나 get 함수 쓰면 동작할때 없더라도 기본 값을 정의 해줄수 있음 

country = person.get("country","알수 없음")
print(f"국적은 {country} 입니다.")

print("before",person.keys())
del person['married']
print("after",person.keys())


