import random

Housekeeping = 0
i = 0

class ObejctOnScreen:

    def RandomCords(self):
        self.x = random.randint(0,1000)
        self.y = random.randint(0,1000)
    def DrawObj(self):
        pass
def GenerateStartDots():
        triangleCorner1 = ObejctOnScreen()
        triangleCorner1.RandomCords()
        triangleCorner2 = ObejctOnScreen()
        triangleCorner2.RandomCords()
        triangleCorner3 = ObejctOnScreen()
        triangleCorner3.RandomCords()

def GenerateStartObj():
    StartObj = ObejctOnScreen()

def CycleOfDrawing():
    pass
def ChangeObj():
    pass

GenerateStartDots()
GenerateStartObj()

while i < 100000:
    ChangeObj()
    CycleOfDrawing()
    i +=1
    print(i)

