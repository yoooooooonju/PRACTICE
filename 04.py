#사전

# cabinet = {3 : "유재석", 100:"김태호"} # key : value
# print(cabinet[3])
# print(cabinet[100])
#
# print(cabinet.get(3))
# # print(cabinet[5]) # 여기서 오류가 나고 프로그램 종료. 뒤에 다른 것들도 실행 안됨
# #print(cabinet.get(5)) # none라고 출력됨. 그리고 뒤에 다른 내용 실행됨
# print(cabinet.get(5, "사용가능")) # 사물함 사용가능 (아무도 쓰는 사람 없다고) 3을 넣으면 유재석 나옴
#
# print(3 in cabinet) # 3이라는 키가 캐비넷에 있냐 없냐
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100": "김태호"}
print(cabinet["A-3"])

#새 손님. 새로운 열쇠 할당
print(cabinet)
cabinet["A-3"] = "김종국" #이러면 김종국이 유재석 키 뺏은거ㅋ..ㅋ
cabinet["c-20"] = "조세호" #새로 지정해줌
print(cabinet)

#손님이 갔어... 그럼 delete 사용

del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 둘 다 출력
print(cabinet.items())

#이제 사물함 다 비어야 할 때 업장 문 닫을 때
cabinet.clear()
print(cabinet) #이제 값이 없으니 빈 중괄호가 나옴

##튜플 (리스트와 달리 내용 변경 불가)
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "workout"
print(name, age, hobby)

(name,age,hobby) = ("김종국", 20, "workout")
print(name, age, hobby)

# 집합 (set) :   중복 안됨. 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # 중복 안되니까 3은 한번만 나옴

java = {"유재석", "김태호","양세형"} #자바 개발자 세명
python = set(["유재석", "박명수"]) #파이선 개발자 두명
# 유재석은 자바랑 파이선 다 있음

#교집합 (자바랑 파이선 모두 가능)
print(java&python)
print(java.intersection(python))

# 합집합 (java나 파이선 둘 중 하나만이라도 할 수 있는...)
print(java|python)
print(java.union(python)) # 순서는 보장 안됨ㅎ

#차집합 (자바는 할 줄 알지만 파이선은 못하는 사람들...)
print(java-python)
print(java.difference(python))

#교육을 받아서 파이선 할 줄 아는 사람들 늘어남
python.add("김태호")
print(python) #세트에 값 추가...

#java를 까먹게된다면...
java.remove("김태호")
print(java) #세트에서 값 빼는 것


##자료구조의 변경

menu = {"커피", "우유", "주스"}
print(menu)
print(menu, type(menu)) #여기서는 자료구조가 set {}

menu = list(menu)
print(menu, type(menu)) #여기서는 자료구조가 list []

menu = tuple(menu)
print(menu, type(menu)) #여기서는 자료구조가 tuple <>

menu = set(menu)
print(menu, type(menu))

# 퀴즈!! 1명 치킨 3명 커피 쿠폰. 조건 1:  n =20, 2: 무작이 추첨, 중복 불가 3: 셔플과 샘플 활용

from random import*
set = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(set)
shuffle(set)
print(set)
set1 = (sample(set,4))
print(set1)
# 중복 하면 안되니까... 따로 뽑는 게 아니라 그냥 한방에 네명을 뽑아

print("--당첨자를 발표합니다 --")
print("치킨 당첨자 : {0}".format(set1[0]))
print("커피 당첨자 : {0}".format(set1[1:]))