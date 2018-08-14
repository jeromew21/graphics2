import time

def test_graphics():
    import graphics
    win = graphics.GraphWin("My Circle", 1500, 600)
    c = graphics.Rectangle(graphics.Point(50,50), graphics.Point(100,100))
    c.draw(win)
    c.setFill("purple")
    win.plot(30, 30, "blue")
    #win.getMouse() # pause for click in window
    #win.close()

def test_graphics2():
    import graphics2 as graphics
    win = graphics.GraphWin("My Circle", 1500, 600)
    c = graphics.Oval(graphics.Point(50,50), graphics.Point(120,100))
    c.draw(win)
    c.setFill("purple")
    win.plot(30, 30, "blue")
    win.getMouse() # pause for click in window
    win.close()

def blind_test(f):
    if f:
        import graphics2 as graphics
    else:
        import graphics
    win = graphics.GraphWin("My Circle", 1500, 600)
    c = graphics.Oval(graphics.Point(50,50), graphics.Point(140,100))
    c.draw(win)
    c.setFill("purple")
    win.plot(30, 30, "blue")
    for i in range(100):
        c.move(1, 1)
    f = graphics.Circle(graphics.Point(400, 400), 70)
    f.setWidth("30")
    f.draw(win)
    k = graphics.Polygon(graphics.Point(40, 40), graphics.Point(40, 80), graphics.Point(80,40))
    k.draw(win)
    win.getMouse() # pause for click in window
    win.close()

blind_test(True)
