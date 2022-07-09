"""
Return example
"""


def main():
    # Variables with type string (str) and integer (int)
    variable_1 = "This is a string"
    variable_2 = 123

    # Call return_function()
    returned_object = return_function(variable_1, variable_2)
    print("Returned object:")
    print(f"{returned_object}")


def return_function(variable_1, variable_2):
    returned_object = (
        f"Variable 1: {variable_1}. Variable 2: {variable_2} is printed as a string."
    )

    # The WRONG way of using return. The statement has the possiblilty of
    # retruning nothing
    if returned_object == "":
        return returned_object
    else:
        None

    # The RIGHT way to use return. No matter what happens returned_object
    # will be returned. The call should always get an expected answer.
    # Use only one return per fuction.
    return returned_object


if __name__ == "__main__":
    main()
