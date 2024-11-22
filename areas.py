def rectangle_area(length, width):
    """Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle (length × width).
    """
    return length * width
def test_should_return_rectangle_area():
    assert  rectangle_area(5, 3) == 15