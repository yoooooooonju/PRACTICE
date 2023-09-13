#if문

#weather = input("오늘 날씨는 어때요?") #input은 사용자의 입력을 받는 문장. 근데 왜... run창에서 입력이 안되지
weather = "눈"
# if 조건:
#     실행 명령문

if weather == "비" or weather =="눈" :
    print("우산을 챙기세요")
elif weather == "미세먼지": #if 비교하고, 그 다음에 elif 비교하고. 그 다음 else(나머지 모든 조건). else가 없으면.. 둘 다 해당 안되면 아무것도 출력 안됨
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요 ")


#temp = int(input("기온은 어때요?")) #머지 왜 안되지
temp = 5
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10<= temp and temp<30:
    print("괜찮은 날씨에요")
elif 0<= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추우니 나가지 마세요")


#for 문 : 반복

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : ...")

for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no)) # 하나씩 값이 들어가는 것...

#순차적으로 커지면 range 라고 할 수 있음. 1-2-3-4-5
for waiting_no in range(1,6): #1,2,3,4,5
    print("대기번호: {0}".format(waiting_no))



#스타벅스에 손님들이 왔다고 치자
starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))


#while : 조건이 만족할 때까지 반복해라
#스벅에서 손님 5번 이상 불렀는데 안오면 버리는 정책이 있다고 해보자...

customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer, index))
    index -=1 #인덱스를 하나씩 줄여나감. 한번 불렀으면 횟수 줄여
    if index == 0:
        print("커피는 폐기처분되었습니다")

#손님이 올 때까지 부르는 카페라고 치자
# customer = "아이언맨"
# index = 1
# while True:
#    # print("{0}, 커피가 준비 되었습니다. 호출{1}회 째입니다.".format(customer, index))
#     # index += 1 이렇게 하면 무한으로......일어난다


#손님이 커피를 찾으러 옴. 이름 확인하고 맞으면 커피 주고 아니면 안줌.

customer = "토르" #토르 커피가 완성됨. 토르 불러야함
person = "Unknown"

while person != customer :
    print ("{0}, 커피가 준비되었습니다. ".format(customer))
    person = input("이름이 어떻게 되세요?") # 토르라고 답해야만 while문에서 탈출이 되는 것. while문은 조건이 만족할 때까지 반복이니까

