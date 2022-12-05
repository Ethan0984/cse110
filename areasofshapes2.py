shape = None
while shape != "quit":
    shape = input("Enter a shape to calculate or enter quit to exit: ").lower()

    if shape == "square":
        sqrlng = int(input("What is the length of the side of a square: "))
        def squarear():
            compute_area_square = sqrlng ** 2
            print(f"The area of this square is {compute_area_square}")
        squarear()

    if shape == "rectangle":
        rectlng = int(input("What is the length of the side of a rectangle: "))
        rectwid = int(input("What is the width of the side of a rectangle: "))
        def rectar():
            compute_area_rectangle = rectlng * rectwid
            print(f"The area of this rectangle is {compute_area_rectangle}")
        rectar()

    if shape == "circle":
        circrad = int(input("What is the radius of the circle: "))
        def circar():
            compute_area_circle = circrad * 2 * 3.14
            print(f"The area of this circle is {compute_area_circle:.2f}")
        circar()