def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height**2)
    if bmi < 18.5:
        category = -1
    elif bmi <= 25.0:
        category = 0
    else:
        category = 1
    print("Your bmi is: " + str(bmi))
    return category

calculate_bmi(weight=57,height=1.73)