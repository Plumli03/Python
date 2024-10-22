import turtle

視窗寬度 = 700
視窗高度 = 700
間距 = 0
數量 = 9 #每行數量

wn = turtle.Screen()
wn.bgcolor("light gray")
wn.setup(width=視窗寬度, height=視窗高度, startx=100, starty=100)
wn.colormode(255)
wn.tracer(0)
skk = turtle.Turtle()
skk.shape('turtle')
skk.hideturtle()
skk.speed(0)

正方形邊長 = ( 視窗寬度 - 間距 * ( 數量 + 1 ) ) / 數量
for row in range( 數量 ) :
    for col in range( 數量 ) :
        skk.penup()
        skk.goto( -視窗寬度/2 + ( col+1 ) * 間距 + 正方形邊長 * ( col+1 ) , \
                   視窗寬度/2 - ( row+1 ) * 間距 - 正方形邊長 * ( row+1 ) )
        skk.setheading(90)
        skk.pendown()

        # if 數量%2==0: #even
        #     if (row == 數量 // 2 - 1 and col == 數量 // 2 - 1) or \
        #         (row == 數量 // 2 - 1 and col == 數量 // 2) or \
        #         (row == 數量 // 2 and col == 數量 // 2 - 1) or \
        #         (row == 數量 // 2 and col == 數量 // 2):
        #         skk.color("yellow")
        #         skk.fillcolor("yellow")
        #     else :
        #         skk.color("red")
        #         skk.fillcolor("red")
        # else:
        #     if row==數量//2 and col==數量//2:
        #         skk.color("yellow")
        #         skk.fillcolor("yellow")
        #     else :
        #         skk.color("red")
        #         skk.fillcolor("red")

        # 設定顏色：黑白相間
        if (row + col) % 2 == 1:
            skk.color("black")
            skk.fillcolor("black")
        else:
            skk.color("white")
            skk.fillcolor("white")

        skk.begin_fill()
        for _ in range(4):
            skk.forward(正方形邊長)
            skk.left(90)
        skk.end_fill()

turtle.done()

# # 初始化 color_list，包含 25 個 "red"
# color_list = ["red"] * (數量**2)
#
# # 將第 13 個顏色設置為 "yellow"
# color_list[((數量**2)//2)] = "yellow"

#
# skk.color(color_list[col+row*數量])  #key串列拿法
# skk.fillcolor(color_list[col+row*數量])