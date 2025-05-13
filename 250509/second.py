
a = [1,2,3,4,5,6,"good"]

for i in a:
    print(i)

for i in range(500): # 9부터 499까지의 범위
    print(i)

for i in range(10,51): # 10부터 50까지의 범위
    print(i)

# range(5000) == range(0,5000,1)  # 오름차순

for i in range(10,1,-1):
    print(i)

"""
1 부터 100까지 출력
2 부터 50까지 짝수만 출력
10 부터 -1까지 출력력
"""

for i in range(1,101):
    print(i)
for i in range(2,51,2):
    print(i)
for i in range(10,-2,-1):
    print(i)

for i in range(1,100): # 1부터 99까지 반복
    if i % 3 == 0: # 3의 배수이면
        print(i) # 3의 배수만 출력


for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
        if i * j == 9:
            print(9)
