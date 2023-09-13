##contunue 와 break (반복문에서 사용됨)

#선생님이 학생들 호명해서 책 읽으라고 하는 상황
absent = [2,5] #결석. 얘네는 책 못읽으니까 이건 넘어가고 다른 애들 책 읽게 함. 이 때 쓰이는 게 continue
no_book = [7] # 책 안가져온 학생
for student in range (1,11): #출석번호가 1부터 10까지 있음
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}, 교무실로".format(student))
        break #뒤에 반복문 있든 없든 여기서 반복문 탈출
    print("{0}, 책 좀 읽어봐".format(student)) # 2,5는 스킵하고 문장 실행. 즉, 컨티뉴는 다음 반복으로 실행하라고 명령하는 것.



# 한 줄 for문
#출석번호가 1,2,3,4 인데 정책이 바뀌어서 앞에 100이 붙음. 101, 102, 103 ...이 되는 거지

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] #students 안에 있는 i 들을 하나씩 불러오면서 거기에 100을 더한 값을 집어넣어라....
print(students)


#학생 이름을 길이로 변환...
students = ["iron man", "thor", "groot"] # 아이언맨 8글자니까 8, 토르 4 이렇게 바꾸고 싶다고
students = [len(i) for i in students] #len은 길이, 문자열의 길이를 의미함.
print(students)


#학생 이름을 대문자로 바꿈...
students = ["iron man", "thor", "groot"]
students = [i.upper() for i in students]
print(students)


##퀴즈!! 50명 승객과 매칭 기회가 있을 때, 총 탑승 승객 구를 구하는 프로그램을 작성해라
# 조건 1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해짐. 조건2: 소요시간 5~15 사이의 승객만 매칭해야 함.

from random import*

count = 0 #총 탑승 승객 수

for i in range(1,51):
    time = randrange(5,51) # 5~50분 소요. 난수.
    if 5<= time <= 15:
        print("[O] {0}번째 손님 (소요시간 :  {1}분)".format(i, time))
        count += 1 #매칭 성공 경우라 카운트 넣음
    else:
        print("[ ] {0}번째 손님 (소요시간 :  {1}분)".format(i, time))

print("총 탑승 승객 수 : {}".format(count))


