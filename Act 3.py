w=int(input("Enter your weight in kg:"))
h=float(input("Enter your height in metre:"))
bmi=w/(h*h)
if bmi<18:
    print("you are underweight")
elif bmi<25:
    print("you are healthy")
elif bmi<30:
    print("you are overweight")
else:
    print("you are obese")