def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #print("Height = ", height) another way to print the same thing but with a comma
    #print("Weight = ", weight) no need for str() function ig

    bmi = weight / (height**2)
    print("BMI = " + str(bmi))

    if(bmi < 18.5):
        print("You are Underweight")
    elif(bmi <= 25.0 and bmi >= 18.5):
        print("You are normal weight")
    elif(bmi > 25.0):
        print("You are overweight")

calculate_bmi(weight=57, height=1.73)
