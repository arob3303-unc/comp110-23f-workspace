"""Turtle Project - A Turtle Scene! Guess the shows while a creeper stares at you."""

__author__ = "730717463"

from turtle import Turtle, update, colormode, done
from random import randint
colormode(255)

# Divide the turtle in four sections
def four_sec(t: Turtle, x: float, y: float) -> None:
    """Divides the turtle screen into four sections for background color."""
    # setting up turtle
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.width(15)
    t.speed("fastest")
    t.pencolor("Black")

    # Top Left Square
    t.fillcolor(229, 250, 171)  # tan color
    t.begin_fill()
    t.right(270)
    i1: int = 0  # index counter

    # loop creates square
    while i1 < 4:
        t.forward(1200)
        t.left(90)
        i1 += 1
    t.end_fill()
    
    # Top Right Square
    t.fillcolor(101, 199, 227)  # light blue
    t.begin_fill()
    i2: int = 0  # index counter

    # loop creates square
    while i2 < 4:
        t.forward(1200)
        t.right(90)
        i2 += 1
    t.end_fill()
    
    t.right(180)  # Change direction of turtle for bottom squares

    # Bottom Left Square
    t.fillcolor(44, 38, 38)  # yellow color
    t.begin_fill()
    i3: int = 0  # index counter

    # loop creates square
    while i3 < 4:
        t.forward(1200)
        t.right(90)
        i3 += 1
    t.end_fill()

    # Bottom Right Square
    t.fillcolor("Black")
    t.begin_fill()
    i4: int = 0  # index counter

    # loop creates square
    while i4 < 4:
        t.forward(1200)
        t.left(90)
        i4 += 1
    t.end_fill()
    

# Draw the first logo (Avatar: The Last Airbender - ATLA)
def arrow(t: Turtle, x: float, y: float) -> None:
    """Draw's Aang's Arrow (ATLA)."""
    # setting up turtle
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed("fastest")
    t.pencolor(98, 240, 240)
    t.fillcolor("White")
    t.width(10)
    t.ht()
    t.right(180)

    # The Arrow
    t.begin_fill()
    t.forward(75)
    t.right(90)
    t.forward(250)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(250)
    t.right(90)
    t.forward(75)
    t.left(120)
    t.forward(250)
    t.left(120)
    t.forward(250)
    t.end_fill()

    # Right Eye
    t.penup()
    t.goto(x + 75, y - 225)
    t.pendown()
    t.pencolor("Black")
    t.fillcolor("White")
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    
    # Left Eye
    t.penup()
    t.goto(x - 225, y - 225)
    t.pendown()
    t.pencolor("Black")
    t.fillcolor("White")
    t.begin_fill()
    t.circle(60)
    t.end_fill()


# Draw the second logo (Designated Survivor)
def america(t: Turtle, x: float, y: float) -> None:
    """Draws Desginated Survivor Flag (USA FLAG)."""
    # setup for the logo
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed("fastest")
    t.pencolor("Black")
    t.fillcolor(219, 3, 3)
    t.width(1)
    t.ht()
    t.right(270)


    # Red Stripe Function
    def red_stripe(t: Turtle, x: float, y: float, f1: float, f2: float, rotation: float) -> None:
        """Function that creates the red stripe design (rectangle)."""
        t.begin_fill()
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.right(rotation)
        i: int = 0  # index counter

        # loop creates an uneven rectangle
        while i < 4:
            if i == 0:
                t.forward(f1)
            elif i == 1:
                t.forward(f2)
            elif i == 2:
                t.forward(f1)
            else:
                t.forward(f2)

            t.left(90)
            i += 1  # increments index
        t.end_fill()

    # Red Stripe 1
    red_stripe(t, x, y, 300, 40, 0)
    # Red Stripe 2
    red_stripe(t, x + 75, y - 100, 500, 40, 0)
    # Red Stripe 3
    red_stripe(t, x + 112.5, y + 50, 250, 40, 180)  # Stripes go down - 180 change in rotation
    # Red Stripe 4
    red_stripe(t, x + 187.5, y + 50, 200, 40, 0)
    # Red Stripe 5
    red_stripe(t, x + 262.5, y + 50, 325, 40, 0)
    # Red Stripe 6
    red_stripe(t, x + 337.5, y + 50, 275, 40, 0)

    # blue square for stars
    t.fillcolor(13, 18, 124)
    t.begin_fill()
    t.penup()
    t.goto(x + 375, y + 50)
    t.pendown()
    t.right(90)

    # loop to create blue square
    i: int = 0
    while i < 4:
        t.forward(262.5)
        t.right(90)
        i += 1
    t.end_fill()

    # Stars for Blue Square Function
    def stars(t: Turtle, x: float, y: float) -> None:
        """Create stars for the flag, was proud of this function."""
        # setup up turtle
        t.fillcolor(101, 199, 227)
        t.pencolor(101, 199, 227)
        t.penup()
        t.goto(x, y)
        t.pendown()

        # variable to increase y
        y1: int = 0
        # index for while loop
        i: int = 0

        # loop creates stars
        while i < 5:  # first while loop allows 5 stars to be made in a column
            t.penup()
            t.goto(x, y + y1)  # y value gets incremented to allow stars to be above each other
            t.pendown()
            i1: int = 0  # index for next while loop
            t.begin_fill()
            while i1 < 5:  # loop creates the actual stars
                t.forward(25)
                t.right(144)
                i1 += 1
            t.end_fill()
            y1 += 40
            i += 1
    
    t.right(90)  # Rotate Turtle to correct side for stars

    # Starting points for stars
    xx: float = 277.5
    yy: float = 360

    # Row 1 for the stars
    stars(t, xx, yy)
    # Row 2
    stars(t, xx + 37.5, yy + 25)
    # Row 3
    stars(t, xx + 75, yy)
    # Row 4
    stars(t, xx + 112.5, yy + 25)
    # Row 5
    stars(t, xx + 150, yy)
    # Row 6
    stars(t, xx + 187.5, yy + 25)
    # Row 7
    stars(t, xx + 225, yy)


# Draw's the third logo (24 - The Show)
def jack(t: Turtle, x: float, y: float) -> None:
    """Draws 24 logo."""
    # Setup for the logo
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed("fastest")
    t.ht()

    # The rectangles function
    def rec(t: Turtle, x: float, y: float, rotate: float, long: bool) -> None:
        """Creates two different lengths of rectangles and are able to rotate it accordingly."""
        i: int = 0
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor(249, 172, 18)
        t.fillcolor(255, 252, 64)
        t.width(5)
        t.right(rotate)  # allows the rectangle to face the right way
        t.begin_fill()
        t.goto(x, y)
        
        if long is True:  # creates a longer rectangle if True
            while i < 2:
                t.forward(150)
                t.right(90)
                t.forward(35)
                t.right(90)
                i += 1
        if long is False:  # creates a shorter rectangle if False
            while i < 2:
                t.forward(75)
                t.right(90)
                t.forward(35)
                t.right(90)
                i += 1
        t.end_fill()
    
    # Draw rectangles for number 2
    rec(t, x, y, 0, True)
    rec(t, x, y + 10, 270, False)
    rec(t, x, y + 130, 90, True)
    rec(t, x + 115, y + 140, 270, False)
    rec(t, x + 150, y + 225, 270, True)

    # Draw rectangles for number 4
    rec(t, x + 360, y - 25, 90, True)
    rec(t, x + 395, y + 135, 270, True)
    rec(t, x + 360, y + 180, 90, False)
    rec(t, x + 280, y + 255, 180, False)


# Draw's the 4th logo (Creeper Face)
def creeper_head(t: Turtle, x: float, y: float) -> None:
    """Draws a creeper head from the game Minecraft."""
    # Setup for the logo
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.speed("fastest")
    t.width(5)
    t.ht()

    # CONSTANTS FOR SQUARES
    NUM_1: int = 63
    NUM_2: int = NUM_1 + 1

    t.pencolor("Black")

    def sq(t: Turtle, x: float, y: float, color: str) -> None:
        """Creates a grid of squares that allows sets up the creeper face (pixels)."""
        # setup the turtle
        t.penup()
        t.goto(x, y)
        t.pendown()

        color_num: int = randint(1, 3)  # allows for random green color - according to the number

        # assigns the color green to the square and creates the loop for square
        if color == "Green":
            # random green color, darker/lighter greens
            if color_num == 1:
                t.fillcolor(43, 132, 5)
            elif color_num == 2:
                t.fillcolor(90, 192, 46)
            elif color_num == 3:
                t.fillcolor(122, 234, 75)

            t.begin_fill()
            i1: int = 0

            # while loop that creates green squares
            while i1 < 4:
                t.forward(NUM_1)
                t.left(90)
                i1 += 1
            t.end_fill()

        # assigns the color black to the square and creates the loop for square
        elif color == "Black":
            t.fillcolor("Black")
            t.begin_fill()
            i2: int = 0

            # loop creates the black squares
            while i2 < 4:
                t.forward(NUM_1)
                t.left(90)
                i2 += 1
            t.end_fill()
    
    # Place the squares (Grid)
    t.right(90)
    i: int = 1

    # x-axis values
    x1: float = x
    x2: float = x
    x3: float = x
    x4: float = x
    x5: float = x
    x6: float = x
    x7: float = x
    x8: float = x

    # y-axis values
    y1: float = y
    y2: float = y - NUM_1
    y3: float = y - NUM_1 * 2
    y4: float = y - NUM_1 * 3
    y5: float = y - NUM_1 * 4
    y6: float = y - NUM_1 * 5
    y7: float = y - NUM_1 * 6
    y8: float = y - NUM_1 * 7

    # Color Variable
    a: str = "Green"
    b: str = "Black"

    # loop that creates the grid of squares: places the correct green and black squares
    while (i <= 64):  # 64 squares 

        # row 1
        if (i <= 8):  # every row is 8 squares
            t.pendown()
            sq(t, x1, y1, a)
            t.penup()
            x1 += NUM_2  # increments the x value to move square over
            i += 1

        # row 2    
        elif (i > 8 and i <= 16):
            t.pendown()
            sq(t, x2, y2, a)
            t.penup()
            x2 += NUM_2
            i += 1

        # row 3    
        elif (i > 16 and i <= 24):
            t.pendown()

            # if i (square number) is at a certain number, black square is placed instead of green
            if i == 18:
                sq(t, x3, y3, b)
            elif i == 19:
                sq(t, x3, y3, b)
            elif i == 22:
                sq(t, x3, y3, b)
            elif i == 23:
                sq(t, x3, y3, b)
            else:  # green squares continue to be placed
                sq(t, x3, y3, a)

            t.penup()
            x3 += NUM_2
            i += 1

        # row 4    
        elif (i > 24 and i <= 32):
            t.pendown()

            if i == 26:
                sq(t, x4, y4, b)
            elif i == 27:
                sq(t, x4, y4, b)
            elif i == 30:
                sq(t, x4, y4, b)
            elif i == 31:
                sq(t, x4, y4, b)
            else:
                sq(t, x4, y4, a)

            t.penup()
            x4 += NUM_2
            i += 1

        # row 5
        elif (i > 32 and i <= 40):
            t.pendown()

            if i == 36:
                sq(t, x5, y5, b)
            elif i == 37:
                sq(t, x5, y5, b)
            else:
                sq(t, x5, y5, a)

            t.penup()
            x5 += NUM_2
            i += 1
        
        # row 6
        elif (i > 40 and i <= 48):
            t.pendown()

            if i == 43:
                sq(t, x6, y6, b)
            elif i == 44:
                sq(t, x6, y6, b)
            elif i == 45:
                sq(t, x6, y6, b)
            elif i == 46:
                sq(t, x6, y6, b)
            else:
                sq(t, x6, y6, a)

            t.penup()
            x6 += NUM_2
            i += 1

        # row 7    
        elif (i > 48 and i <= 56):
            t.pendown()
            
            if i == 51:
                sq(t, x7, y7, b)
            elif i == 52:
                sq(t, x7, y7, b)
            elif i == 53:
                sq(t, x7, y7, b)
            elif i == 54:
                sq(t, x7, y7, b)
            else:
                sq(t, x7, y7, a)

            t.penup()
            x7 += NUM_2
            i += 1

        # row 8    
        elif (i > 56 and i <= 64):
            t.pendown()
            
            if i == 59:
                sq(t, x8, y8, b)
            elif i == 62:
                sq(t, x8, y8, b)
            else:
                sq(t, x8, y8, a)

            t.penup()
            x8 += NUM_2
            i += 1


def main() -> None:
    """The entrypoint to my scene."""
    #  turtles for each scene
    bg_color: Turtle = Turtle()  # background turtle
    avatar: Turtle = Turtle()  # first turtle
    designated_survivor: Turtle = Turtle()  # second turtle
    show_24: Turtle = Turtle()  # third turtle
    creeper: Turtle = Turtle()  # fourth turtle

    # scenes
    four_sec(bg_color, 0, 0)  # background scene
    arrow(avatar, -200, 350)  # first logo scene
    america(designated_survivor, 150, 300)  # second logo scene
    jack(show_24, -550, -380)  # third logo scene
    creeper_head(creeper, 55, -10)  # fourth logo scene

    update()
    done()  # turtle done drawing


if __name__ == "__main__":
    main()