import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
    
def art():
    window = turtle.Screen()
    window.bgcolor("green")
    #create instance of Class Turtle
    move = turtle.Turtle()
    move.color("blue")
    move.shape("arrow")
    move.speed(2)
    for i in range(1,37):
        draw_square(move)
        move.right(10)
    
       
    window.exitonclick()

art()
