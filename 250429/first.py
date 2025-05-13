'''
input으로 키와 몸무게를 입력받는다. (숫자형으로 변환)
키가 130 이하이면 "키 미만"을 출력하고, 몸무게가 10 이상이면 정상"을 출력하세요.
'''

# print("키를 입력하세요")
# cm = input()
# print("몸무게를 입력하세요")
# kg = input()

# print(kg,cm)

# len(cm) # len(변수)는 변수의 문자 수를 가져온다.

"""
input() 두 번을 사용하여, 두개의 변수의 임의의 문자열을 넣고,
len() 을 사용하여 문자의 수를 변수에 넣는다.

'첫번째 변수의 문자 수는 {문자의 수} 입니다.'
'두번째 변수의 문자 수는 {문자의 수} 입니다.'
"""

# print("첫번째 문자열을 입력하세요")
# string = input()
# print("두번째 문자열을 입력하세요")
# string2 = input()

# stringlen = len(string)
# stringlen2 = len(string2)

# print(f"첫번째 변수의 문자 수는 {stringlen} 입니다.")
# print(f"두번째 변수의 문자 수는 {stringlen2} 입니다.") 

money = 10000000000
print(f"{money:,} 원 갖고싶어요.")

# and 연산
## 다른 언어에서는
# a && b
a = True
b = True
c = a and b
d = 10 > 5 and 10 < 5 # 
print(d)

f = 10 >= 10 or False # or 앞의 내용이 이미 True이기에 뒤에 어떤 조건이 오던 True
print(f)

f = False and True and True # 0 1 1
print(f)

f2 = (False or True) and True # 1 1
print(f2)

f3 = not((False or True) and True) # 0 (1 1) 
print(f3)

a = 10
b = 20

c = a!=b #다르니? 라고 물어보는것 # True
d = not a!=b # 다르니? 라고 물어보는것을 반전 # False


# 멤버연산
st = "modulabs is good"
sta = "good" in st
stn = "good" not in st
print("?:",sta, stn)

num = "123456-1234567-good"
num1,num2, strs = num.split("-")
print(num1, num2, strs)

#코드업6045 정수 끊어출력
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
sum = a + b + c
avg = sum/3

print(f"{sum} {avg:.2f}")

# if문
age = 10
if age > 18:
    print("성인입니다.")
print("안녕하세요.")

age = 19
if age <= 19:
    print("청소년입니다.")
elif age < 30:
    print("성인입니다.")
else:
    print("30대가 아닙니다.")


'''
한줄에 생년월일(yyyymmdd)가 공백을 기준으로 입력된다.
년도가 짝수라면 "짝수년도에 태어났습니다." 아니라면 "홀수년도에 태어났습니다" 출력
'''

print("생년월일을 yyyy mm dd 형식으로 띄어쓰기하여 입력해주세요.")
yyyy, mm, dd = input().split(" ")
y,m,d = int(yyyy),int(mm),int(dd)
if y % 2 == 0:
    print("짝수")
else:
    print("홀수")