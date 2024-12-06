"""
Author : Mehmet Yucel
Student Number: 759742
Revison date : 6 December 2024
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
    # Initialize mod_string variable
    mod_string = ""
    # List of bad characters
    badChars = ['"', ',']
    # Strip the line
    ln = ln.strip()
    # Loop through characters
    for c in ln:
        # Check if character is not in bad characters list
        if c not in badChars:
            # Add character to mod_string
            mod_string = mod_string + c
    # Return mod_string
    return mod_string

"""
Plots a point on the canvas at the point and color given
T (turtle) = The turtle object
x (int) = X coordinate
y (int) = Y coordinate
d (int) = Size of the dot
color (str) = Color of the dot
"""
def plotIt(T, x, y, d, color):
    # Raises the pen to prevent drawing
    T.penup()
    # Goto the given coordinates
    T.goto(x, y)
    # Lowers the pen to being drawing
    T.pendown()
    # Puts a dot of size d and color
    T.dot(d, color)
    # Raises the pen to prevent drawing
    T.penup()

"""
Draws the image on the canvas based off the image data
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
    # Set x and y half to negative value of half of the rows/cols (so image can be centered)
    x_half = int(-cols // 2)
    y_half = int(-rows // 2)
    # Loops through x values of image
    for x in range(len(img)):
        # Increase y_half counter by 1
        y_half += 1
        # Loops through y values of image
        for y in range(len(img[x])):
            # Plot the point on canvas using plotIt function
            plotIt(t, x_half * pixel_size * x_rot, -y_half * pixel_size * y_rot, pixel_size, img[x][y])
            # Increase x_half counter by 1
            x_half += 1
        # Reset x_half counter for next iteration
        x_half = int(-cols // 2)

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
    # Initialize image data list
    imageData = []
    # Loop through number of rows
    for i in range(rows):
        # Read the line and set to row variable
        row = fh.readline()
        # Modify the string to get rid of unwanted characters
        row = modify(row)
        # Initialize row array
        rowArr = []
        # Loop through each character/symbol in thr row
        for j in range(len(row)):
            color = row[j]
            # Compare symbol to colorDefs list and set to the right color
            for k in range(numColors):
                if color == colorDefs[k][0]:
                    color = colorDefs[k][1]
            # Add the color to the row array
            rowArr.append(color)
        # Add the row array to the imageData list
        imageData.append(rowArr)
    # Return imageData
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
    # Initialize colorDefs list
    colorDefs = []
    # Loop through number of colors
    for i in range(numColors):
        # Read the line and set to colorLine
        colorLine = fh.readline()
        # Modify the string to get rid of unwanted characters
        colorLine = modify(colorLine)
        # Split the colorLine into symbol, c, and color
        sym, c, color = colorLine.split()
        # Check if sym is ~  and change it to a space
        if sym == '~':
            sym = ' '
        # Add color and symbol to colorDefs list
        colorDefs.append([sym, color])
    # Return colorDefs
    return colorDefs

# Initialize filename and rotate variables
filename = ""
rotate = False

# Set valid to false
valid = False
# Loop until a valid option is chosen
while not valid:
    # Prompt user to choose an option
    user_input = input("Choose an option: \nA: rocky_bullwinkle_mod.xpm  B: smiley_emoji_mod.xpm  C: Enter a file name \n")
    # Check if user chose option A
    if user_input.lower() == 'a':
        # Set filename and valid to true
        filename = "rocky_bullwinkle_mod.xpm"
        valid = True
    # Check if user chose option B
    elif user_input.lower() == 'b':
        # Set filename and valid to true
        filename = "smiley_emoji_mod.xpm"
        valid = True
    # Check if user chose option C
    elif user_input.lower() == 'c':
        # Promt user to choose a filename and set valid to true
        filename = input("Enter the file name: ")
        valid = True

fh = None
try:
    # Open the chosen file for reading
    fh = open(filename, "r")
except:
    # File is not found and exit the program
    print("File not found.")
    exit()

# Set valid to false
valid = False
# Loop until a valid option is chosen
while not valid:
    # Prompt user to choose if they want to rotate the image
    user_input = input("Would you like to rotate the image (Y/N): ")
    # Check if user chose yes
    if user_input.lower() == 'y':
        # Set rotate and valid to true
        rotate = True
        valid = True
    # Check if user chose no
    elif user_input.lower() == 'n':
        # Set valid to true
        valid = True

# Read the first line of the file
colorData = fh.readline()
# Modify the line to get rid of unwanted characters
colorData = modify(colorData)
# Initialize variables for columns, rows, and number of colors
cols, rows, numColors = (0,0,0)
# Split the color data into columns, rows, and number of colors
if len(colorData.split()) == 4:
    cols, rows, numColors, temp = colorData.split()
else:
    cols, rows, numColors = colorData.split()

# Convert rows, columns, and number of colors to int
rows = int(rows)
cols = int(cols)
numColors = int(numColors)

# Call getColorData function and set it to colorDefs
colorDefs = getColorData(fh, numColors)
# Call getImageData function and set it to imageData
imageData = getImageData(fh, rows, colorDefs)
# Close the file
fh.close()

# Print the dimensions of the image
print("\nDimensions: %d x %d" % (rows, cols))
# Print the number of colors
print("Number of colors:", numColors)
# Print the color definitions
print("Colors:", colorDefs)
# Draw the image, and rotate if rotate is true
if rotate:
    drawImage(imageData, 3, rows, cols, -1, -1)
else:
    drawImage(imageData, 3, rows, cols, 1, 1)
turtle.update()
