from graphics import *
from graphics import Line, Point, GraphWin, Text, Polygon
import math

def getlines(win):
    for i in range(11): #loop to create the 11x11 grid
        line2 = Line(Point(0, i), Point(10, i))
        line = Line(Point(i, 0), Point(i, 10))
        line.draw(win)
        line2.draw(win)
    
def main():
    #opening up the window with specific coordinates
    win = GraphWin ( "Draw a Triangle",401,401)
    win.setCoords (-0.1 , -0.1 , 10.1 , 10.1)
    message = Text (Point (5 , 0.5 ), "Click on four points")
    message.draw(win)

    #creating each point for the rectangle/two triangles
    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)
    p4=win.getMouse()
    p4.draw(win)

    #calling the line function
    getlines(win)

    #designing both triangle to connect to each other
    triangle = Polygon (p1 , p2 , p3)
    triangle.setFill("peach puff" )
    triangle.setOutline("cyan")
    triangle.draw (win)
    triangle2= Polygon(p1, p3, p4)
    triangle2.setFill("blue")
    triangle2.setOutline("blue")
    triangle2.draw(win)
    
    #creating each distance formula for all the sides
    d=((p1.getX()-p2.getX())**2 + (p1.getY()-p2.getY())**2)**0.5
    d2=((p2.getX()-p3.getX())**2 + (p2.getY()-p3.getY())**2)**0.5
    d3=((p3.getX()-p1.getX())**2 + (p3.getY()-p1.getY())**2)**0.5
    d4=((p4.getX()-p3.getX())**2 + (p4.getY()-p3.getY())**2)**0.5
    d5=((p4.getX()-p1.getX())**2 + (p4.getY()-p1.getY())**2)**0.5
    d6=((p1.getX()-p4.getX())**2 + (p1.getY()-p4.getY())**2)**0.5

    #setting up the area formula for both triangles using Heron's formula
    s1 = (d + d2 + d3) / 2
    area1 = round((s1 * (s1 - d) * (s1 - d2) * (s1 - d3)) ** 0.5,4)

    s2 = (d4 + d5 + d6) / 2
    area2 = round((s2 * (s2 - d4) * (s2 - d5) * (s2 - d6)) ** 0.5,4)

    area = round(area1 + area2, 4)

    #printing out the new area
    message2=Text(Point(5, 2), f"Area1={area1}\nArea2={area2}\nTotal Area={area}\n")
    message2.draw(win)
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()
if __name__=="__main__":
    main()
