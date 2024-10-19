import random

def calculate_energy_optimization(energy_used, soc):
    if soc < 20:
        return "Warning: Low battery! Charge soon."
    
    if energy_used > 50:
        return "Consider smoother acceleration to save energy."
    
    return "Good job! You're optimizing energy usage well."

# Simulate getting vehicle data
energy_used = random.uniform(10, 60)
soc = random.uniform(10, 100)

# Calculate recommendations
recommendation = calculate_energy_optimization(energy_used, soc)
print(recommendation)
