## 문제 31: 사칙연산 계산기
a, b = map(int,input("연산할 두 수를 입력하세요.").split())
oper = input("연산자를 입력하세요.")

if oper == "+":
    print(a,"+",b,"=",a+b)
elif oper == "-":
    print(a,"-",b,"=",a-b)
elif oper == "*":
    print(a,"*",b,"=",a*b)
elif oper == "/":
    print(a,"/",b,"=",a/b)


## 문제 32: 세금 계산기
price = int(input("금액을 입력하세요."))
per = int(input("세율을 입력하세요."))
print(f"세금: {price*(per/100)} \n세후금액: {price-price*(per/100)}")


## 문제 33: 논리 연산 테이블
def boolean_operations(a, b):
    print(f"{a} AND {b} => {a and b}")
    print(f"{a} OR {b}  => {a or b}")
    print(f"NOT {a}     => {not a}")
    print(f"NOT {b}     => {not b}")

# 사용자 입력 받기
a_input = input("첫 번째 불리언 값을 입력하세요 (True/False): ")
b_input = input("두 번째 불리언 값을 입력하세요 (True/False): ")

# 문자열을 실제 불리언 값으로 변환
a = a_input.strip().capitalize() == "True"
b = b_input.strip().capitalize() == "True"

# 연산 실행
boolean_operations(a, b)

## 문제 34: 할인 계산기
a_input = int(input("원래 가격 입력: "))
b_input = int(input("할인율 입력: "))
print(f"할인금액: {a_input*(b_input/100)}원")
print(f"최종가격: {a_input-(a_input*(b_input/100))}원")

## 문제 35: 큰 수 판별
a, b, c = map(int,input("세 개의 숫자 공백으로 입력:").split())
print(max(a,b,c))

## 문제 36: 윤년 판별
year = int(input("연도 입력:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,"년은 윤년입니다.")
else:
    print(year,"년은 윤년이 아닙니다.")

## 문제 37: 문자열 포함 여부
a_text = input("첫번째 문자열 입력")
b_text = input("두번째 문자열 입력")
if b_text in a_text:
    print(f"{a_text}에 {b_text}이(가) 포함되어 있습니다.")
else:
     print(f"{a_text}에 {b_text}이(가) 포함되어 있지 않습니다.")


## 문제 38: 조건부 출력
a = int(input("점수 입력:"))
if a >= 90:
    print("학점: A")
elif a >= 80:
    print("학점: B")
elif a >= 70:
    print("학점: C")
elif a >= 60:
    print("학점: D")
else:
    print("학점: F")

## 문제 39: 자릿수 합계
num = input("양의 정수를 입력하세요: ")
print("각 자릿수의 합은:", sum(map(int, num)))

## 문제 40: 복합 조건
age = int(input("나이: "))
member = input("회원 여부 (Y/N): ")
if age >=19 and member == "N":
    print("입장료: 10000원")
elif age >=19 and member =="Y":
    print("입장료: 8000원")
else:
    print("입장료: 5000원")