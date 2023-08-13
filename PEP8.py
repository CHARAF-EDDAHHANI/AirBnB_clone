def calculate_square_area(side_length):
    """Calculate the area of a square."""
    return side_length ** 2

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    import math
    return math.pi * radius ** 2

def main():
    """Main function to demonstrate area calculations."""
    side = 5
    radius = 3

    square_area = calculate_square_area(side)
    circle_area = calculate_circle_area(radius)

    print(f"Area of square with side {side}: {square_area}")
    print(f"Area of circle with radius {radius}: {circle_area}")

if __name__ == "__main__":
    main()
