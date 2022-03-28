# BMI Calculator

# BMI = weight/height **2

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg's: "))

bmi = weight / height **2
bmi_t = round(bmi)

if bmi_t <= 18.5:
    print(f"Your BMI is {bmi_t}, you are underweight.")
elif bmi_t <= 25:
    print(f"Your BMI is {round(bmi_t)}, you have a normal weight.")
elif bmi_t <= 30:
    print(f"Your BMI is {round(bmi_t)}, you are slightly overweight.")
elif bmi_t <=35:
    print(f"Your BMI is {round(bmi_t)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi_t)}, you are clinically obese.")