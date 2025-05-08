## 문제 1: 인ㅏㅏ기
name = input()
print(name)

## 문제 2: 에코 프로그램
a = input()
print(a*3)

## 문제 3: 나이 계산기
year = int(input())
age = 2025 - year
print(f"당신의 나이는 {age}입니다.")

## 문제 4: 원 넓이 계산
a = int(input())
one = 3.14**a
print(f"반지름이 5인 원의 넓이 : {one}")

## 문제 5: 여행 거리 계산
km, h = map(int, input("시속과 시간을 입력하세요.: ").split())
print(f"총 이동거리: {km*h}km")

## 문제 6: 문장 합치기
a = input("안녕하세요를 입력하세요")
b = input("반갑습니다를 입력하세요")
print(a,b)

## 문제 7: 인치-센티미터 변환
a = int(input("인치를 입력하세요."))
print(f"{a}인치는 {a*2.54}센티미터 입니다.")

## 문제 8: 팁 계산기
price = int(input("식사 금액을 입력하세요."))
per = int(input("팁 비율을 입력하세요."))
temp = price*(per/100)
tip = int("{:g}".format(temp)) # 불필요한 소수점 제거
print(f"팁 금액: {tip} \n총 지불 금액: {price + tip}") 

## 문제 9: BMI 계산기
cm = int(input("키를 입력하세요.")) * 0.01
kg = int(input("몸무게를 입력하세요."))
bmi = kg / (cm ** 2) ## 제곱
print(f"BMI: {bmi:.2f}") ## 소수점 둘째자리까지 출력

## 문제 10: 다중 입력
list = list(map(int, input("숫자 여러개를 공백으로 구분하여 입력하세요.: ").split()))
print(f"첫 번째 숫자: {list[0]} \n마지막 숫자: {list[-1]}") # 마지막 요소는 인덱스 -1