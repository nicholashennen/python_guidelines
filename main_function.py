"""
Simple Program Start.
Use checking for if __name__ == "__main__" can help prevent unwanted app
execution.
Use function main() as a driver to call other functions and classes.
"""


def main():
    print("function main called.")

    # Call second_function()
    second_function()


def second_function():
    print("A second function was called from function main.")


if __name__ == "__main__":
    main()
