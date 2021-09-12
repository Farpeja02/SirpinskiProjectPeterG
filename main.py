import random
import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.hideturtle()
t.speed(100000)
turtle.screensize(0,800)
i = 0
amountOfCorners = 3
listOfCorners = []

class ObejctOnScreen:

    def __init__(self):
        self.x = random.randint(0,400)
        self.y = random.randint(0,400)
    def DrawObj(self):
        t.goto(self.x,self.y)
        t.dot(3)


def GenerateStartDots():
        global amountOfCorners
        for x in range(amountOfCorners):
            listOfCorners.append(ObejctOnScreen())

def GenerateStartObj():
    global startObj
    startObj = ObejctOnScreen()

def CycleOfDrawing():
    startObj.DrawObj()
def ChangeObj():
    randomCorner = random.randint(0, 2)
    ChosenCorner = listOfCorners[randomCorner]
    startObj.x = (startObj.x + ChosenCorner.x) / 2
    startObj.y = (startObj.y + ChosenCorner.y) / 2


GenerateStartDots()

c = 0
for corner in listOfCorners * 2:
    if c == 0:
        t.penup()
    else:
        t.pendown()
    t.goto(corner.x,corner.y)
    c += 1
t.penup()

GenerateStartObj()
while i < 100000:
    ChangeObj()
    CycleOfDrawing()
    i =+1
