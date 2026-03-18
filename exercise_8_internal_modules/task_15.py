# Task 15: Calculate BMI from user-entered weight and height;
# handle invalid input exceptions.

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if value <= 0:
                print("Value must be greater than 0. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_bmi(weight, height):
    return round(weight / height**2, 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "You are underweight"
    elif 18.5 <= bmi <= 24.9:
        return "You are normal weight"
    elif 25 <= bmi <= 29.9:
        return "You are overweight"
    else:
        return "You are obese"


def main():
    weight = get_float_input("What is your weight (in kg)? ")
    height = get_float_input("What is your height (in meters)? ")
    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi}")
    print(bmi_category(bmi))


if __name__ == "__main__":
    main()
