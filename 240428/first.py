a = 10
b = 20
c = 0
d = 40

print(type(a),type(b),type(c),type(d))
print(int(9.33333))

number1 = 3.12
number2 = 0.12
print(type(number1),type(number2))
print(float(3))

str1 = "큰따옴표문자열"
str2 = '작은따옴표문자열'
str3 = '''
긴 문자열
오늘은 4월 28일 입니다.
5월이 멀지 않았네요.
'''

print(str1,str2)
print(type(str3))
print(str3)
      
# 개인정보 출력해보기
name = "Nayoung"
fname = "Choi"
birth = "250924"
num = "3412353"
id = "email"
domain1 = "gmail.com"
domail2 = "naver.com"
print("이름:",fname,name)
print("주민등록번호:",birth,"-",num)
print(f'email:{id}@{domain1}')

#문자열 반복하기
str10 = str1*10
test2 = "30"
print(str10)
# print(str1*test2) #타입이 일치하지 않아 에러

print(f"오늘은{a}월{b*10}일입니다.")

#문자열 인덱싱
s = "life is good"
print(s[0])
print(s[3])
##print(s[300])

#문자열 슬라이싱 [start:stop:step]
print(s[0:3])
print(s[0:3:2])

#다양한 슬라이싱 방법
s = 'weniv CEO licat'
print(1, s[0:5]) #0번째 인덱스부터 4번째 인덱스까지 출력
print(2, s[6:]) #6번째 인덱스부터 끝까지 출력
print(3, s[:]) #전체출력
print(4, s[::-1]) #전체 중 역순출력
print(5, s[::2]) #전체 중 2개식 건너뛰고 출력


s = 'ip address = 172.100.200.100'
'''
1. ip address 문자열을 슬라이싱 기법을 활용해 변수에 담아 출력
2. a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 답는다
3. f-string 을 활용해서 172100200100 이 나오게 하기 '
'''
print(1, s[0:10])
a = s[13:16]
b = s[17:20]
c = s[21:24]
d = s[25:]
print(2,a,b,c,d)
print(f"IP Addresss=,{a}.{b}.{c}.{d}")

# 입력 구현 
# 주의! 파이썬에서는 무조건 string 타입으로 입력이 받아진다.
'''
입력을 몇가지 변수에 담아서 
f-string, 문자붙이기, 문자반복하기 등 여러 기술을 활용해 출력하세요
'''

# print("이름을 입력하세요")
# name = input()
# print("나이를 입력하세요")
# age = input()
# print(f"이름:{name}, 나이:{age}")

#형변환
# print(type(a))
# b=int(a)
# print(type(b))

#형변환 필요할 경우 새로운 변수를 만들어 할당하여 원데이터의 변형이 없게 방지한다.


#문자열 고유 기능
s = 'weniv CEO licat'
print(s.lower())
print(s.upper())
print(s.find("good"))#값을 찾을 수 없기 때문에 -1
#print(s.index("good")) #error: substring not fount
print(s.find("weniv")) #찾을 수 있기 때문에 0
print(s.find("licat")) 
print(s.index("weniv")) #0번째 인덱스
print(s.index("licat")) #10번째 인덱스
s2 = s.replace("CEO","CTO")
print(s2)

s3 = "weniv-corp"
s4 = s3.split("-")
print(s4)

# 입력받아 출력하기 실습
# print("키, 몸무게, 성별, 나이, 이름 순으로 띄어쓰기하여 입력해주세요")
# info = input()
# cm,kg,gender,age,name = info.split()
# print(f"키:{cm},몸무게:{kg},성별:{gender},나이:{age},이름:{name}")
# print(f"이름:{name*3}")

a=1
b=0
c=-1
d="okay"
f=""
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(f))
print(a==b)
x = None

result = 5+3
print(result)

result = 3+2.5
print(result)

print(11/2)
print(10/2)
print(type(10/2)) # 몫과 나머지 모두 구하기에 5.0이라는 실수로 판단
print(11//2)
print(11%2)

print(10**3)
print(10^1)