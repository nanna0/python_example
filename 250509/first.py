# 복습

a = (1, 10, 1, 2, 3) # 튜플은 중복을 허용한다.

# 슬라이싱
b = a[2:5] # (1,2,3)
c = a[1] # 10

# 기능
c = a.count(1) # 2
d = a.index(1) # 0 , 1이라는 값이 여러개 있지만 첫번째 인덱스만 반영.

# set 자료구조 (중복 허용x)
a = {1, 2, 3, 1}
print(a) # {1, 2, 3} 만 출력. 중복된 값은 하나만 출력된다.


a = [1, 1, 1, 2, 2, 3] # list 에서 중복값을 제거하고 싶을 때 자료형을 set 으로 바꾼다.
b = set(a)
c = list(b) # 중복 제거된 데이터를 다시 list로 바꾼다.

a = {1,2,3}
# print(a[0]) # set 은 index 기능이 없다. TypeError: 'set' object is not subscriptable

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"합집합: {set1 | set2}") # 합집합: {1, 2, 3, 4, 5, 6, 7, 8} 중복을 제거한 값
print(f"교집합: {set1 & set2}") # 교집합: {4, 5}
print(f"차집합: {set1 - set2}") # 차집합: {1, 2, 3}
print(f"차집합: {set2 - set1}") # 차집합: {8, 6, 7}

print(f"대칭 차집합: {set1.symmetric_difference(set2)}")
print(f"set1이 set2의 부분집합인가? {set1.issubset(set2)}")

# 딕셔너리 dict()
my_dict = {"me":"길동"}
my_dict2 = dict()
#my_dict2_1 = dict({("하나":"one"), ("둘":"two")})
#print(my_dict2_1)

# 데이터 추가
dict4 = dict()
dict4["max"] = [1, 2, 3, 4]
print(dict4)

'''
dict() 를통해 빈 딕셔너리를 만든 후

데이터 삽입을 하여 키가 4개 , 각각의 밸류에는 다른 타입의 데이터를 넣어서

그 딕셔너리를 출력
'''

mydict = dict()
mydict["fruit"] = "사과"
mydict["food"] = "츄러스"
mydict["key"] = "value"
mydict["num"] = 17
mydict["array"] = [a, b, c]
print(mydict)


# 데이터 읽기
person = {'name' : 'licat', 'age' : 25, 'height':'165.5'}
print(f"이름은: {person["name"]} 입니다.")
print(f"나이는: {person["age"]} 입니다.")
# print(f"생년월일은: {person["birth"]}입니다.") KeyError : 'birth'

# 데이터 수정
person["age"] = 30
person["weight"] = 100
print(person)

# 데이터 삭제
del person["height"]
print(person)
# value 값을 지울 땐 
# person["key"] = None

b = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}

# b = {"good1": {"good2": [1, 2, 3, [1, 2, 3, 4]]}} 처럼 나오게 만들려면?
b["good1"]["good2"][3].append(4)
print(b)

# get(키,키가 없을 경우의 value)
city = person.get('city',"없는뎅")
print(city)
city2 = person.get('city2',"없는뎅")
print(city2)

person = {"name": "licat", "age": 25, "city": "seoul"}
# 키만 가져온다.

person_keys = person.keys() #키 값들만 추출
print(person_keys) # dict_keys(['name', 'age', 'city'])
a = list(person_keys) # 형변환
print(a)

# value 만추출
person_values = person.values() # 밸류 값들만 추출
print(person_values) # dict_values(['licat', 25, 'seoul'])
b = list(person_values)
print(b)

# 전체를 추출
person_items = person.items()
print(person_items) #dict_items([('name', 'licat'), ('age', 25), ('city', 'seoul')])
c = list(person_items) #[('name', 'licat'), ('age', 25), ('city', 'seoul')]
print(c)
print(type(person_items))
#del person['age'] 권장 x
a = person.pop("age") # age라는 키에 있는 값을 a에 저장장
print(a)