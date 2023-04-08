# 구구단

dan = int(input("단을 입력하세요: "))
result_val = ""
for i in range(1,10):
    # 이스케이프 문자 - '\n'
    current_val = f'{dan} x {i} = {dan*i}\n'
    result_val = result_val + current_val
print(result_val)


"""
# 전체 구구단(2~9단)
start_dan = int(input("시작단 입력: "))
end_dan = int(input("끝단 입력: "))

for i in range(start_dan, end_dan+1):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
    print()
"""
"""
# 중첩 for문
for i in range(0, 5): # 0,1,2,3,4    
    for j in range(0,5):
        print('*', end = '')
    print() # 줄바꿈
"""
"""
*
**
***
****
*****
"""
"""
for i in range(0, 5): # 0,1,2,3,4    
    for j in range(0, i):
        print('*', end ='')
    print() # 줄바꿈
"""
"""
*****
****
***
**
*
"""


for i in range(0, 5): # 0,1,2,3,4    
    for j in range(0, 5-i): # 5-0, 5-1, 5-2...
        print('*', end ='')
    print() # 줄바꿈    

"""
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20

i = 0 j = 1, 2, 3, 4, 5            -> 5*0 + 1
i = 1 j = 6, 7, 8, 9, 10          -> 5*1 + 1
i = 2 j = 11, 12, 13, 14, 15 -> 5*2 + 1
"""

for i in range(0,4):
    for j in range(1,6):
        num = (5*i)+j
        print(num+j, end = ' ')
    print()


