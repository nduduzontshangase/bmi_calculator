# BMI Calculator

# BMI = weight/height **2

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg's: "))

bmi = weight / height **2
bmi_t = round(bmi)

print(f"Your bmi is {bmi_t}.")