# ## 문제 41: 비밀번호도 강도 검사
# def is_valid_password(password):
#     if len(password) < 8:
#         return False

#     has_letter = False
#     has_digit = False

#     for char in password:
#         if char.isalpha():
#             has_letter = True
#         elif char.isdigit():
#             has_digit = True

#     return has_letter and has_digit

# # 사용자로부터 비밀번호 입력받기
# password = input("비밀번호를 입력하세요: ")

# if is_valid_password(password):
#     print("유효한 비밀번호입니다.")
# else:
#     print("비밀번호는 8자 이상이어야 하며, 문자와 숫자를 모두 포함해야 합니다.")


# ## 문제 42: 단어 뒤집기
# word = input("단어를 공백으로 구분하여 입력하세요:").split()
# reversed_word = [words[::-1] for words in word] 
# print(reversed_word)

## 문제 43: 문자 카운터
# text = input("문자 입력")
# vowel = "aeiouAEIOU" # 모음
# consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  # 자음

# vowel_count = 0 # 초기화
# consonant_count = 0 

# for char in text:
#     if char in vowel:
#         vowel_count += 1
#     elif char in consonant:
#         consonant_count += 1

# print(f"모음 개수: {vowel_count}")
# print(f"자음 개수: {consonant_count}")

# ## 문제 44: 근삿값 계산
# a = float(input("실수를 입력하세요."))
# print("가장 가까운 정수:" ,round(a))

## 문제 45: 날짜 유효성 검사


    
