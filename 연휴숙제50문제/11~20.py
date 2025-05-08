## 문제 11: 변수 교환
a, b = map(int, input("두 숫자를 입력하세요.: ").split())
print(f"교환 전: a = {a}, b = {b}")
a, b = b, a
print(f"교환 후: a = {a}, b = {b}")

## 문제 12: 문자열 정보 출력
string = input("문자열 입력")
print(f"문자열 길이: {len(string)}\n첫 글자: {string[0]}\n마지막 글자: {string[-1]}")

# 문제 13: 이니셜 만들기
fname, lname = input("이름의 성과 이름을 공백으로 입력하세요.").split()
print(f"이니셜: {(fname.upper())[0]}.{(lname.upper())[0]}")

## 문제 14: 소수점 자릿수
number = float(input("실수를 입력하세요."))
print(f"{number:.2f}")

## 문제 15: 나이 구간 판별
age = int(input("나이를 입력하세요."))
if age >= 65:
    print("노년")
elif 35 <= age or age >= 64:
    print("중장년")
elif 19 <= age or age >= 34:
    print("청년")
else:
    print("미성년자")

## 문제 16: 문자열 분석
def analyze_string(s):
    space_count = 0
    digit_count = 0
    letter_count = 0

    for char in s:
        if char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1

    print(f"공백 수: {space_count}")
    print(f"숫자 수: {digit_count}")
    print(f"문자 수: {letter_count}")

user_input = input("문자열을 입력하세요: ")
analyze_string(user_input)

## 문제 17: 참/거짓 변환
str = input("다양한 값을 입력해보세요.")
print(bool(str)) ## 문제 기준이 뭔지 모르겠음.

## 문제 18: 홀짝 판별
a = int(input("숫자를 입력하세요."))
if a % 2 == 0:
    print(f"{a}은(는) 짝수입니다.")
else:
    print(f"{a}은(는) 홀수입니다.")

## 문제 19: 문자열 분할
string = input("문자를 공백으로 구분하여 입력하세요.").split()
print(','.join(string))

## 문제 20: 온도 단위 변환기
tem_input = int(input("온도를 입력하세요."))
unit = input("단위를 C와 F중 입력하세요.")
if unit == "C":
    tem = tem_input * 9/5 + 32
    print(f"{tem_input}°C 는 {tem}°F 입니다.")
elif unit == "F":
    tem = (tem_input - 32) * 5/9
    print(f"{tem_input}°F 는 {tem}°C 입니다.")
else:
    print("정확한 단위를 입력하세요.")

