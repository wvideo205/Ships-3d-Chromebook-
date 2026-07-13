


EXPECTED_BAKE_TIME = 40 

def bake_time_remaining(time_left):
    """Calculates the amount of cooking time left """
    return EXPECTED_BAKE_TIME - time_left


def preparation_time_in_minutes(number_of_layers):
    """ Why are we still here """
    return number_of_layers * 2
   

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
        """
    layers_time = number_of_layers * 2 
    return layers_time + elapsed_bake_time

    
