name = input("Enter your name: ")
weight_kg = float(input("Enter weight in kg: "))  
height_ft = float(input("Enter height in feet: ")) 
height_in = height_ft * 12  # Convert feet to inches

# Convert weight to pounds
weight_lb = weight_kg * 2.20462

# bmi calculation using pounds and inches
bmi = (weight_lb * 703) / (height_in ** 2)

print("Your bmi is:", round(bmi, 2))

if bmi > 0:
    if bmi < 18.5:
        print(name + ", you're underweight. It's important to maintain a healthy diet and consult a healthcare professional.")
    elif bmi <= 25:
        print(name + ", you're in the normal weight range. Keep up the good work and stay healthy!")
    elif bmi < 30:
        print(name + ", you're overweight. Consider exercising more and balancing your diet for better health.")
    elif bmi >= 30:
        print(name + ", you're obese. It may be a good idea to focus on fitness and nutrition for overall well-being.")
    elif bmi < 35:
        print(name + ", you're Class 1 obese. Health improvements are possible with gradual lifestyle changes.")
    elif bmi < 40:
        print(name + ", you're Class 2 obese. It's essential to seek medical advice for a safe and effective plan.")
    else:
        print(name + ", you're Class 3 obese (Severe Obesity). It's important to consult with a healthcare professional to manage your health.")
else:
    print("Please enter a valid input.")
