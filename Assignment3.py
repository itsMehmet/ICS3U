"""
Author : Carter Wells
Student Number: 756118
Revison date : 26 November 2024
Program : Making a graphics plotter in Turtle
Description : A program that will plot the pixels of a given xpm file
    using Turtle
VARIABLE DICTIONARY :
    filename (str) = The file name/path for the xpm file
    rotate (bool) = Boolean value of if the image will be rotated
    valid (bool) = Boolean value of if the user has entered valid input
    user_input (str) = User input in type string
    colorData (str) = String value of the first line
    rows (int) = Number of rows
    cols (int) = Number of cols
    numColors (int) = Number of colors
    colorDefs (list) = Array of the colors and symbols
    imageData (list) = Array of each line in the image with colors
"""

# Imports turtle 
import turtle
# Sets turtle background color
turtle.bgcolor("gray40")
# Turns off updates to speed up plotting
turtle.tracer(0,0)
# Sets turtle to t variable
t = turtle.Turtle()
# Hides the plotter sprite
t.hideturtle()

"""
Modifies a string to get rid of unwanted characters (" and ,)
ln (str) = String input into function
mod_string (str) = New string to be returned
badChars (list) = List of not wanted characters
"""
def modify(ln):
    mod_string = ""
    badChars = ['"', ',']
    ln = ln.strip()
    for c in ln:
        if c not in badChars:
            mod_string = mod_string + c
    return mod_string

"""
Plots a point on the canvas at the point and color input
T (turtle) = The turtle object
x (int) = X coordinate
y (int) = Y coordinate
d (int) = Size of the dot
color (str) = Color of the dot
"""
def plotIt(T, x, y, d, color):
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.dot(d, color)
    T.penup()

"""
Draws image on the canvas with input of imageData list
img (list) = The imageData list with each of the colors needed to plot
pixel_size (int) = Size of each dot
rows (int) = Number of rows
cols (int) = Number of cols
x_rot (int) = X rotation
y_rot (int) = Y rotation
x_half (int) = Half of the x value (starting at negatve)
y_half (int) = Half of the y value (starting at negative)
"""
def drawImage(img, pixel_size, rows, cols, x_rot, y_rot):
    x_half = int(-cols / 2)
    y_half = int(-rows / 2)
    for x in range(len(img)):
        y_half += 1
        for y in range(len(img[x])):
            plotIt(t, x_half * pixel_size * x_rot, -y_half * pixel_size * y_rot, pixel_size, img[x][y])
            x_half += 1
        x_half = int(-cols / 2)

"""
Returns imageData as a list
fh = File header
rows (int) = Number of rows
colorDefs (list) = Array of the colors and symbols
imageData (list) = List of each of the rows and colors to be returned
rowArr (list) = Eacg of the colors in one row
color (str) = The color/symbol
"""
def getImageData(fh, rows, colorDefs):
    imageData = []
    for i in range(rows):
        row = fh.readline()
        row = modify(row)
        rowArr = []
        for j in range(len(row)):
            color = row[j]
            for k in range(numColors):
                if color == colorDefs[k][0]:
                    color = colorDefs[k][1]
            rowArr.append(color)
        imageData.append(rowArr)
    return imageData

"""
Returns a list of the colors and symbols
fh = File header
numColors (int) = Number of colors to be read from file
colorDefs (list) = Array of the colors and symbols to be returned
sym (str) = The symbol of the color
color (str) = The color represented by the symbol
"""
def getColorData(fh, numColors):
    colorDefs = []
    for i in range(numColors):
        colorLine = fh.readline() 
        colorLine = modify(colorLine)
        sym, c, color = colorLine.split()
        if sym == '~':
            sym = ' '
        colorDefs.append([sym, color])
    return colorDefs

filename = ""
rotate = False

valid = False
while not valid:
    user_input = input("Choose an option: \nA: rocky_bullwinkle_mod.xpm  B: smiley_emoji_mod.xpm  C: Enter a file name \n")
    if user_input.lower() == 'a':
        filename = "rocky_bullwinkle_mod.xpm"
        valid = True
    elif user_input.lower() == 'b':
        filename = "smiley_emoji_mod.xpm"
        valid = True
    elif user_input.lower() == 'c':
        filename = input("Enter the file name: ")
        valid = True

valid = False
while not valid:
    user_input = input("Would you like to rotate the image (Y/N): ")
    if user_input.lower() == 'y':
        rotate = True
        valid = True
    elif user_input.lower() == 'n':
        valid = True
    
fh = open(filename, "r")

colorData = fh.readline()
colorData = modify(colorData)
cols, rows, numColors = (0,0,0)
try:
    cols, rows, numColors = colorData.split()
except:
    cols, rows, numColors, temp = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)

colorDefs = getColorData(fh, numColors)
imageData = getImageData(fh, rows, colorDefs)
fh.close()

print("\nDimensions: %d x %d" % (rows, cols))
print("Number of colors:", numColors)
print("Colors:", colorDefs)
if rotate:
    drawImage(imageData, 3, rows, cols, -1, -1)
else:
    drawImage(imageData, 3, rows, cols, 1, 1)
