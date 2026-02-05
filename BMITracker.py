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
