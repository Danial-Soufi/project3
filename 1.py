import turtle

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.penup()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def sierpinski(points, degree, my_turtle):
    if degree == 0:
        
        draw_triangle([points[0], midpoint(points[0], points[1]), midpoint(points[0], points[2])], 'blue', my_turtle)

        draw_triangle([midpoint(points[0], points[1]), points[1], midpoint(points[1], points[2])], 'red', my_turtle)
        
        draw_triangle([midpoint(points[0], points[2]), midpoint(points[1], points[2]), points[2]], 'green', my_turtle)
    else:
        
        sierpinski([points[0], midpoint(points[0], points[1]), midpoint(points[0], points[2])], degree-1, my_turtle)
        sierpinski([midpoint(points[0], points[1]), points[1], midpoint(points[1], points[2])], degree-1, my_turtle)
        sierpinski([midpoint(points[0], points[2]), midpoint(points[1], points[2]), points[2]], degree-1, my_turtle)

def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor('white')  
my_points = [[-200, -100], [0, 200], [200, -100]]  
sierpinski(my_points, 4, my_turtle)  
my_screen.exitonclick()
