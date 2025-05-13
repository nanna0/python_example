# c = [1, "2", "good", 4, [1, 2, 3, [123, "good"],31],2]
# # 1. good이라는 문자열을 인덱싱 기법으로 추출
# # 2. 슬라이싱 기법을 통해 [123,"good"] 을 추출

# print(c[2])
# print(c[4][3][1],c[4][3][0:2])



# a = [3,2,3, 'aaaa',1,2,3,4,5,'good']

# a[3] = "aaaa"

# ## a[3][1] = "g" # agaa 문자열의 특정 문자는 바꿀 수 없다.


# li = [1,2,3]
# li.clear() # 리스트 안에 있는 데이터만 삭제
# print(li)



# """
# 빈리스트를 만든다.
# append를 사용하여 이중 리스트를 만든다.
# 출력한다.
# 리스트의 데이터를 다 지운다.
# 출력한다.
# copy를 활용한다.
# 카피를 활용한 리스트에 append를 사용하여 출력한다.
# """
# # 빈 리스트
# list = []

# # append 사용하여 이중 리스트 생성
# list.append(1)
# list.append([3])

# # 리스트 출력
# print(list)

# #리스트 클리어
# list.clear()
# list.append("a")
# list.append("b")

# list2 = list.copy()

# print(list)
# print(list2)

# # count
# lista = [1,2,3,"okay",1,1,1]
# print(lista.count(1)) # 4

# listb = [1, 2, 3, [1, 2, 3, 1]]
# print(listb.count(1) + listb[3].count(1))

# a = ["good", "okay"]
# # b = a.index("aaaa") # Value Error : 'aaaa' is not in list
# ## 예외처리
# try: 
#     a.index('aaa')
# except:
#     print("에러")
# c = a.index("okay") #배열은 find 불가
# print(c)


# a.insert(0,0)
# print(a)
# b = a.pop()
# print(a)
# if len(a) >= 1: # 리스트 내부의 데이터 갯수가 1개 이상이라면?
#     a.pop() # 추출
# else:
#     print("리스트가 비어있습니다.")

'''
기존에 데이터가 있는 리스트를 만든다.
insert를 활용해서 데이터를 넣는다.
pop을 사용하여 꺼낸 데이터를 출력한다.
remove를 사용하여 특정 데이터를 제거해본다.
'''

# listA = ["a","b","c","d"]
# listA.insert(4,"e")
# print(listA)

# listA.pop()
# print(listA)

# listA.remove("a")
# print(listA)

a = [1, 2, 3, 4, 5]
b = list(reversed(a))
print(a)
print(b)
c = a[::-1]
print("========================")
# sort sorted

a = [5, 4, 3, 2, 1]
# a.sort() 원본데이터 자체를 변경

b = list(sorted(a)) # 원본 데이터 복사후 정렬 -> 리스트 타입으로변경
print(a)
print(b)
c = [1,2,3,4,5]
# sorted(리스트, reverse=bool)
sorted(c,reverse=False) # sorted(a)
print(c)
d = list(sorted(c, reverse=True))
print(d)

