class HydrationTracker:
  # HydrationTrackeris a python class created to calculate and track daily water intake for users
  def __init__(self, user_name: str, weight_kg: float):
        self.user_name = user_name
        self.weight_kg = weight_kg
        self.RECOMMENDED_INTAKE_ML = calculate_recommended_intake(weight_kg)
        self.total_intake_ml = 0
        self.intake_log = []
  
  
