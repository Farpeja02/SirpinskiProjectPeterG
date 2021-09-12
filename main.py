import random
import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.hideturtle()
t.speed(100000)
turtle.screensize(0,800)
Housekeeping = 0
i = 0
n = 3
listOfCorners = []

class ObejctOnScreen:

    def __init__(self):
        self.x = random.randint(0,400)
        self.y = random.randint(0,400)
    def DrawObj(self):
        t.goto(self.x,self.y)
        t.dot(3)


def GenerateStartDots():
        global n
        for x in range(n):
            listOfCorners.append(ObejctOnScreen())

def GenerateStartObj():
    global StartObj
    StartObj = ObejctOnScreen()

def CycleOfDrawing():
    StartObj.DrawObj()
def ChangeObj():
    RandomCorner = random.randint(0,2)
    ChosenCorner = listOfCorners[RandomCorner]
    StartObj.x = (StartObj.x + ChosenCorner.x) / 2
    StartObj.y = (StartObj.y + ChosenCorner.y) / 2


GenerateStartDots()
GenerateStartObj()
c = 0
for corner in listOfCorners * 2:
    if c == 0:
        t.penup()
    else:
        t.pendown()
    t.goto(corner.x,corner.y)
    c += 1

t.penup()

while i < 100000:
    ChangeObj()
    CycleOfDrawing()
    i =+1