class HydrationTracker:
  # HydrationTrackeris a python class created to calculate and track daily water intake for users
  def __init__(self, user_name, weight_kg):
        self.user_name = user_name
        self.weight_kg = weight_kg
        self.RECOMMENDED_INTAKE_ML = calculate_recommended_intake(weight_kg)
        self.total_intake_ml = 0
        self.intake_log = []  

    def add_water(self, amount_ml):
        # Add water intake in milliliters
        if amount_ml <= 0:
            raise ValueError("Water intake must be greater than 0 ml")

        self.total_intake_ml += amount_ml
        self.intake_log.append(amount_ml)
      
    def get_total_intake(self):
        return self.total_intake_ml      
