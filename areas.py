import math
def rectangle_area(length, width):
    """Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle (length × width).
    """
    return length * width
def triangle_area(base, height):
    """Calculates the area of a triangle.

    Args:
        base: The base of the triangle.
        height: The height of the triangle.

    Returns:
        The area of the triangle (0.5 × base × height).
    """
    return 0.5 * base * height

def circle_area(radius):
    """Calculates the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle (π × radius²).
    """
    return math.pi * radius**2
def test_should_return_rectangle_area():
    assert  rectangle_area(5, 3) == 15
def test_should_return_triangle_area():
    assert triangle_area(8, 4) == 16
def test_should_return_circle_area():
    assert circle_area(2) == math.pi * 2**2