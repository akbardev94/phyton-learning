import turtle
trtl = turtle.Turtle ()
turtle.bgcolor("Black")  
trtl.speed(0) 
turtle.title("Design")  
def drawRainbow():
    for i in range(500):    
        trtl.color('white') 
        trtl.backward(i)    

        trtl.left(110)      
    trtl.color("white")     
    trtl.hideturtle()       
    trtl.setpos((20,0))     
drawRainbow()

