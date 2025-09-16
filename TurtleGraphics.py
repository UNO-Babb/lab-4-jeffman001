#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(pent, sides, size):
    for s in range(sides):
        pent.forward(size)
        pent.right (360/sides)

#def fillCorner(greg, corner):
#    drawSquare(greg, 100)
#    if corner == 1:
#        greg.begin_fill()
#        drawSquare(greg, 50)
#        greg.end_fill()
#    if corner == 2:
#        greg.forward(50)
#        greg.begin_fill()
#        drawSquare(greg, 50)
#        greg.end_fill()
#    if corner == 3:
#        greg.forward(100)
#        greg.right(90)
#        greg.forward(50)
#        greg.begin_fill()
#        drawSquare(greg, 50)
#        greg.end_fill()
#    if corner == 4:
#        greg.right(90)
#        greg.forward(50)
#        greg.left(90)
#        greg.begin_fill()
#        drawSquare(greg, 50)
#        greg.end_fill()

#def squaresInSquares (bob, num):
 #   bob.penup()
  #  bob.goto(-50, 50)
   # bob.pendown()
    #drawSquare(bob, 100)
    #if num > 0:
     #   up = 25
      #  left = -25
       # square = 50
       # for n in range(num-1):
        #    bob.penup()
         #   bob.goto(-50 + left, 50 + up)
          #  bob.pendown()
           # drawSquare(bob, 100 + square)
           # up = up + 25
           # left = left - 25
           # square = square + 50
            
    
def main():
    myTurtle = turtle.Turtle()
    #drawSquare(myTurtle, 100)
    #drawPolygon(myTurtle, 8, 100) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
