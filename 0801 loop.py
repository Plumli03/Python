import turtle

wn = turtle.Screen()
wn.bgcolor("plum")
wn.title("Turtle6663629")
skk = turtle.Turtle()
skk.shape('turtle')
# skk.color('black') #線顏色
skk.speed(0)

# color_list=['aquamarine','cyan','lavender']
# for n in range(3): #0-2 共3個
#     skk.penup()
#     skk.goto(300-50*n,0)
#     skk.setheading(90)
#     skk.pendown()
#
#     skk.fillcolor(color_list[n])
#     skk.begin_fill()
#     skk.circle(300-50*n)
#     skk.end_fill()

color_list=['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4'
    ,'LightCyan2', 'LightCyan3', 'LightCyan4',
    'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4' ]

print(len(color_list))

import random
color_list=random.sample(color_list,15)

for n in range(30): #0-2 共3個

    skk.color(color_list[n%10])  # 線顏色color_list[n%10]
    skk.penup()
    skk.goto(300-n*5,-300+n*5)
    skk.setheading(90)
    skk.pendown()

    skk.fillcolor(color_list[n%10]) #取餘數Mod
    skk.begin_fill()
    skk.forward(600-10*n)
    skk.left(90)
    skk.forward(600-10*n)
    skk.left(90)
    skk.forward(600-10*n)
    skk.left(90)
    skk.forward(600-10*n)
    skk.left(90)
    skk.end_fill()

skk.penup()
skk.goto(0,0)
turtle.done()
