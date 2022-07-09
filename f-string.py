"""
f-string example
"""


def main():
    number = 3
    name = "Bob"
    fruit = "apple"

    # f-string
    print(f"{name} has {number} {fruit}s.")

    # Not using an f-string
    print(name + " has " + str(number) + " " + fruit + "s.")


if __name__ == "__main__":
    main()
