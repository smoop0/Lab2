def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #print("Height = ", height) another way to print the same thing but with a comma
    #print("Weight = ", weight) no need for str() function ig

    bmi = weight / (height**2)
    print("BMI = ", round(bmi,2))

    print("Weight Classification: ", end="")

    if(bmi < 18.5):
        print("Underweight")
    elif(bmi <= 25.0 and bmi >= 18.5):
        print("normal weight")
    elif(bmi > 25.0):
        print("overweight")

calculate_bmi(weight=20, height=1.73)
print("=============================>")
calculate_bmi(weight=57, height=1.73)
print("=============================>")
calculate_bmi(weight=90, height=1.73)
