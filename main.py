import random
import turtle

screen = turtle.getscreen()
turtleObj = turtle.Turtle()
turtleObj.hideturtle()
turtleObj.speed(100000)
turtle.screensize(0,800)

amountOfCorners = 3
listOfCorners = []

class ObjectOnScreen:

    def __init__(self):
        self.x = random.randint(0,400)
        self.y = random.randint(0,400)
    def DrawObj(self):
        turtleObj.goto(self.x, self.y)
        turtleObj.dot(3)


def GenerateStartDots():
        global amountOfCorners
        for x in range(amountOfCorners):
            listOfCorners.append(ObjectOnScreen())

def GenerateStartObj():
    global startObj
    startObj = ObjectOnScreen()

def CycleOfDrawing():
    startObj.DrawObj()
def ChangeObj():
    randomCorner = random.randint(0, 2)
    ChosenCorner = listOfCorners[randomCorner]
    startObj.x = (startObj.x + ChosenCorner.x) / 2
    startObj.y = (startObj.y + ChosenCorner.y) / 2


GenerateStartDots()

controlPenUp = 0
for corner in listOfCorners * 2:
    if controlPenUp == 0:
        turtleObj.penup()
    else:
        turtleObj.pendown()
    turtleObj.goto(corner.x, corner.y)
    controlPenUp += 1
turtleObj.penup()

GenerateStartObj()
AmountOfRounds = 0
while AmountOfRounds < 100000:
    ChangeObj()
    CycleOfDrawing()
    AmountOfRounds =+1
