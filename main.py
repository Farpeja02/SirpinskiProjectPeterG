import random
import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.hideturtle()
t.speed(100000)
turtle.screensize(0,500)
Housekeeping = 0
i = 0
n = 3
listOfCorners = []

class ObejctOnScreen:

    def __init__(self):
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)
    def DrawObj(self):
        t.goto(self.x,self.y)
        t.dot(5)


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
    StartObj.x = StartObj.x + ChosenCorner.x / 2
    StartObj.y = StartObj.y + ChosenCorner.y / 2
GenerateStartDots()
GenerateStartObj()
for corner in listOfCorners:
    t.goto(corner.x,corner.y)

t.penup()

while i < 1000:
    ChangeObj()
    CycleOfDrawing()
    i =1