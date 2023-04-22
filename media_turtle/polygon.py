# 다각형 만들기
import turtle as t

def polygon(n):
    for i in range(n):
        t.forward(50)
        t.left(360/n) # 다각형의 한개의 내각

def polygon2(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360/n)  # 다각형의 한개의 내각

# main 영역
# 함수 호출
# polygon(변의개수)
polygon(3)
polygon(5)

t.up() # 펜 올리기
t.forward(100)
t.down() # 펜 내리기

polygon(3)
# polygon2(변의개수, 거리)
polygon2(3,100)
polygon2(5,100)



t.mainloop()