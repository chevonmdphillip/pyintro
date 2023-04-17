"""Prints "Hello World!" to the console."""


def square(num_x: float) -> float:
    """
    :param x: float
    :return: float
    Returns the square of a number.
    """
    return num_x ** 2


def main():
    """
    :return: None
    Prints "Hello World!" to the console.
    """
    print(square(2))


if __name__ == "__main__":
    main()
