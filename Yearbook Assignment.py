""" Author : Mehmet Yucel
Revison date : 24 Oct 2024
Program : School Yearbook
Description : A program that computes the minimum area and dimensions for photos with 
1x1 units being placed in a yearbook.
VARIABLE DICTIONARY :
min_perimeter (int) = Stores the smallest perimeter found for a valid arrangement of the photos
best_x (int) = The width of the rectangle that gives the minimum perimeter
best_y (int) = The height of the rectangle that gives the minimum perimeter
N (int) = The number of photographs input by the user
user_input (str) = The raw input from the user, which can be a number or the string "done"
perimeter (int) = The calculated perimeter of the rectangle for the current arrangement of photos
x (int) = One dimension (width) of the rectangle for the current arrangement of photos
y (int) = The other dimension (height) of the rectangle for the current arrangement of photos """


import math

def find_min_perimeter(N):
   
    min_perimeter = N * 2
    best_x = 1
    best_y = N
    
    
    for x in range(1, math.floor(math.sqrt(N)) + 1):
        if N % x == 0: 
            y = int(N / x)
            perimeter = 2 * (x + y) 
            if perimeter < min_perimeter: 
                min_perimeter = perimeter
                best_x = x
                best_y = y
    
    return min_perimeter, best_x, best_y



user_input = ""
while user_input.lower() != "done":
    user_input = input("Please input your number of photographs: ")
    
    if user_input.lower() == "done": 
        print("Goodbye!")
    else:
        try:
            N = int(user_input)
            if N <= 0: 
                print("is not a valid number of photos. Please enter a positive number.")
            else:
                perimeter, x, y = find_min_perimeter(N)
                print("Minimum perimeter is %d with dimensions: %d x %d" % (perimeter, x, y))
        except: 
            print("Invalid input. Please enter a valid number or 'done' to quit.")
                
