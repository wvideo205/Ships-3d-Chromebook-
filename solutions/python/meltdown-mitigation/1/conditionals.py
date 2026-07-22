"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature > 800 or temperature == 800:
        return False 
    elif float(neutrons_emitted) < 500 or neutrons_emitted == 500:
        return False 
    elif float(temperature * neutrons_emitted) > 500000 or (temperature * neutrons_emitted) == 500000:
        return False 
    else :
        return True 


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current 
    efficiency_score = (generated_power / theoretical_max_power) * 100 
    if efficiency_score >= 80:
        return "green"
    elif efficiency_score < 80 and efficiency_score >= 60 :
        return "orange"
    elif efficiency_score < 60 and efficiency_score >= 30 :
        return "red"
    else :
        return "black"
    
 
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if (temperature * neutrons_produced_per_second) == threshold or (temperature * neutrons_produced_per_second) <= (1.1 * threshold) and (temperature * neutrons_produced_per_second) >= (0.9 * threshold):
        return "NORMAL"
    else:
        if (temperature * neutrons_produced_per_second) < (0.9 * threshold):
            return "LOW"
        else : 
            return "DANGER"
  
