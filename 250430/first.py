## 10:45 수업시작; 

# a = 10
# b = 20

# if a > 10:
#     print("good")
# elif b == 20:
#     print("20입니다.")
# elif a == 10:
#     print("10입니다")
# else:
#     print("이도저도아니다.")


'''
split() 활용

a,b 변수를 활용,
키,몸무게를 입력받는다.

키와 몸무게를 나눈 나머지를 출력한다.

조건문을 활용해서

키(a)가 130 이상이면 a, 150이상이면 b, 170 이상이면 c 180 이상면이면 d를 출력하세요
'''
# cm, kg = map(int, input("키와 몸무게를 입력하세요.: ").split()) # map을 사용하여 입력, 프린트, 형변환 동시에
# d = cm%kg
# print( "키와몸무게를 나눈 나머지 출력:", d)
# if cm >= 180: # 큰 수 부터 체크하는게 중요하다.
#     print("d")
# elif cm >=170:
#     print("c")
# elif cm >=150:
#     print("b")
# elif cm >=130:
#     print("a")
# else:
#     print("키는 130보다 작습니다.")


# 시험 점수 입력하기
'''
시험 점수를 입력받아 90~100점은 A, 80~89점은 B, 70~79점은 C, 60~69점은 D, 나머지 점수는 F 를 출력하는 프로그램을 작성하시오
시험 점수는 0보다 크거나 같고 100보다 작거나 같은 정수.
'''

# score = int(input("시험 점수 입력(0~100): "))

# if score >=90:
#     print("A")
# elif score >=80: 
#     print("B")
# elif score >=70: 
#     print("C")
# elif score >=60: 
#     print("D")
# else:
#     print("F")

## and or 연산활용

a = 10
b = 20

if a == 10 and b == 20: # 둘 다 참이어야 한다.
    print("good")
else:
    print("no")


'''
a, b, c 를 입력받는다.
a가 100이고 b가 200이상이면 "a"를 출력
b가 1이면 "b"를 출력
이도저도 아니면 c를 출력
'''

# a, b, c = map(int, input().split())
# if a == 100 and b >= 200:
#     print("a")
# elif b == 1:
#     print("b")
# else:
#     print("c")

'''
백준 2480번 주사위 세개
'''
# a,b,c = map(int,input().split())
# if a==b==c:
#     print(10000+a*1000)
# elif a==b or a==c:
#     print(1000+a*100)
# elif b==c:
#     print(1000+c*100)
# # else:
# ##    print(max(a,b,c)*100)
# else: 
#     price = 0 ## price를 우선 0으로 만들어 대비한다.
# ## max를 쓰지 않고 최대값 구하기
# if a != b and b != c and a != c:
#     temp = 0
#     if b > temp:
#         temp = b
#     if c > temp:
#         temp = c
#     price = temp * 100

# print(f"상금: {price}원") 

li = [10,20,30,40]
a = "a씨"
b = "b씨"
 
x = [1, 2, 3]
y = ['apple', 'banana', 'cherry', 1]
z = [1, [2], 3] in [2]
print(z)


## 리스트 실습
print("어제 만들어먹은 집코바 레시피")
ingredients = ["닭다리살", "파", "양배추",]
sauce = [["고춧가루2", "다진마늘1"]
         , [["맛술2","고추장1","간장2","굴소스1"]
            ,["물엿2","설탕2","케찹1"]]]

print(f"기름에 {ingredients} 를 먼저 굽고, {sauce[0]}를 넣은 후 {sauce[1][0]}과 {sauce[1][1]}를 뿌린다.")


## 수정
t3 = [5, 4, 3, [2, 1]]
[1,2,3,[4,5]] 

t3[0] = 1
t3[1] = 2
t3[3] = [4,5]

print(t3)

t4 = []
t4.append(1) # 추가
t4.clear() # 리스트 데이터 삭제

t4 = [5,4,3,2,1]
t4.sort()
print(t4)