def polygon(t, s, d):
    a = 360/s#angle variable is inside the function
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.right(a)
    t.end_fill()
def rightcurve(t):
    
    for n in range(20):
        t.begin_fill()
    
        t.circle(n)
        t.forward(n)
        t.left(n)
        t.end_fill()

def leftcurve(t):
    for n in range(20):
        t.begin_fill()
    
        t.circle(n)
        t.forward(n)
        t.right(n)
        t.end_fill()

def stars(t):
    for times in range(11):
        star(t,times *10 + 8,c)
        t.penup()
        t.right(30)
        t.forward(50)
        t.pendown()


