# 튜플(tuple)의 생성 및 관리
t1 = (1,) # 값 1개 저장할때 콤머를 사용
print(t1)
t2 = (2, 3, 4)
print(t2)
t1 = t1 + t2
print(t1)

# 인덱싱과 슬라이싱 (리스트와 동일)
print(t1[0]) # 1
print(t1[0:]) # (1 2 3 4)
print(t1[1:2]) # ( 2, )

# 수정 불가
# t1[0]=5

# 삭제 불가
del t1[1]
