num_sides = int(input("Enter the number of sides the shape has: "))

if num_sides == 3:
    print("This is a triangle, a very balanced and stable shape")
elif num_sides == 4:
    print("This is a square or rectangle, with four corners that represent the four corners of the world ")
elif num_sides == 5:
    print("This is a pentagon, they are hard to draw nicely")
elif num_sides == 6:
    print("This is a hexagon, nothing special here")
elif num_sides == 7:
    print("This is a septagon, a shape that doesn't appear often")
elif num_sides == 8:
    print("This is an octagon, a common shape in math problems")
elif num_sides == 9:
    print("This is a nonagon, a not so common shape in math problems")
elif num_sides == 10:
    print("This is a decagon, counting the sides of this shape uses up all your fingers")
else:
    print("ERROR. OUTSIDE OF RANGE")