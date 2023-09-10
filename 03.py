#리스트 []

#지하철을 탔는데 칸별로 10명, 20명, 30명 있다고 치자
subway1 = 10
subway2 = 20
subway3 = 30

subway =[10,20,30] #서브웨이라는 하나의 리스트 안에 이 세 개를 묶어준 것
print(subway)

subway = ["유재석","박명수","정형돈"]
print(subway)
print(subway.index("박명수")) #박명수가 몇 번째 칸에 타고 있는가. 0, 1, 2

#하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하") #append = 더함 맨 뒤에
print(subway)

# 노홍철을 유재석, 박명수 사이에 넣음
subway.insert(1, "노홍철") #1번 위치에 노홍철을 넣겠다고.
print(subway)

#뒤에서부터 한 명씩 빼볼게
print(subway.pop()) #맨 뒤에 사람이 누구냐고 (사라질 사람)
# print(subway) #하하 없어짐
#
# print(subway.pop()) #맨 뒤에 사람이 누구냐고 (사라질 사람)
# print(subway)
#
# print(subway.pop()) #맨 뒤에 사람이 누구냐고 (사라질 사람)
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인

subway.append("유재석")
print(subway)
print(subway.count("유재석")) #같은 값이 몇 번 나오는지

#정렬

num_list = [5,2,4,3,1]
num_list.sort()
# print(num_list) #순서대로 정렬
#
# num_list.reverse() #반대로 정렬
# print(num_list)
#
# num_list.clear()
# print(num_list) # 모두 지워서 빈 리스트가 됨

#다양한 자료형 함께 사용 가능

mix_list = ["유재석", 20, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list) # num리스트랑 mix리스트랑 합친건가
print(num_list)