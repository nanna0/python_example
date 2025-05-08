## 문제 21: 대소문자 변환
str = input("문자열을 입력하세요.")
print(f"대문자: {str.upper()}\n소문자: {str.lower()}\n첫 글자만 대문자: {str.title()}")

## 문제 22: 문자열 슬라이싱
str = input("문자열을 입력하세요.")
print(f"앞 3글자: {str[0:3]}\n뒤 3글자: {str[-3:]}\n거꾸로: {str[::-1]}")

# 문제 23: 단어 위치 찾기
str = input("문장입력:")
find = input("찾을 단어 입력:")
string = str.replace(" ","")
print(f"단어 {find}의 위치: {string.find(find)}") # 자동으로 없을 경우 -1 반환

# 문제 24: 문자 교체
user_input = input("문장입력")
txt = input("어떤 문자를 수정하고 싶으신가요?")
n_txt = input("무엇으로 수정하고 싶으신가요?")
print(user_input.replace(txt,n_txt))

## 문제 25. 문자 출현 횟수
usr_input = input("문장 입력")
find = input("찾을 문자 입력")
print(f"문자{find}의 출현 횟수: {usr_input.count(find)}")

## 문제 26. 이메일 유효성 검사
email = input("이메일 주소 입력")
if "@" in email and "." in email:
    print("유효한 이메일 입니다.")
else: 
    print("유효하지 않은 이메일 입니다.")

## 문제 27: 문자열 패딩
string = input("문자열 입력:")
len = int(input("원하는 길이 입력"))
print(string.ljust(len,'*'))

## 문제 28: 문자열 중앙 문자
text = input("문자열 입력:")
length = len(text)
mid = length // 2
if length % 2 == 0:
    # 짝수면 가운데 두 글자 출력
    print(text[mid - 1:mid + 1])
else:
    # 홀수면 가운데 한 글자 출력
    print(text[mid])

## 문제 29: 특수문자 제거
def remove_special_chars(text):
    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~"
    for char in special_chars:
        text = text.replace(char, '')
    return text

input_text = input("특수문자를 포함한 문장 입력")
cleaned_text = remove_special_chars(input_text)
print(cleaned_text)

# 문제 30: 이스케이프 시퀀스 연습
print("그녀가 말했다: \"안녕하세요!\" \n이름 나이 직업 \n홍길동\t30\t개발자 \n안녕! \n반가워요!")

