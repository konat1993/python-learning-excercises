# Task 2: Access a list index out of range and handle IndexError exception.
try:

    try:
        data_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        data_list[10]
    except IndexError:
        raise ValueError("Index out of range.")
except Exception as e:
    print(e)
