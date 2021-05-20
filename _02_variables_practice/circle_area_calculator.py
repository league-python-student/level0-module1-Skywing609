import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    radius = input("What radius do you want your circle to be?")
    sides = input("How many sides do you want in your polygon?")
    # Make a new turtle
    blob = turtle.Turtle()
    blob.circle(int(radius), 360, int(sides) )
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    blob.penup()
    # Call the turtle .penup() method
    blob.goto(80, 5)
    # Move your turtle to a new x,y position using .goto()
    math.pi
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle

    # Call turtle.done()
