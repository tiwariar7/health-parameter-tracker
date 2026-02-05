class BMITracker:
    # BMITracker is a python class created to calculate and track Body Mass Index (BMI)
    def __init__(self, weight_kg, height_cm):
        self.weight_kg = weight_kg
        self.height_cm = height_cm

    def calculate_bmi(self):
        # This is a python function curated especially for BMI calculation
        # Standard Formula for BMI : BMI = weight (kg) / (height (m))^2
        if self.height_cm <= 0:
            raise ValueError("Height must be greater than zero.")
        if self.weight_kg <= 0:
            raise ValueError("Weight must be greater than zero.")
        height_m = self.height_cm / 100
        bmi = self.weight_kg / (height_m ** 2)
        return bmi

    def bmi_category(self):
        # This function curated tocategorize the BMI value into standard categories
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"
