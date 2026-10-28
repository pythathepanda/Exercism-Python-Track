def value(colors):
    """Function used to determine the value of the resistor"""
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    color_duo = list(colors)
    
    resistor_value = ""
    for color in color_duo:
        if color_duo.index(color) <= 1:
            if color in color_list:
                resistor_value += str(color_list.index(color))

    resistor_value = int(resistor_value)
    return resistor_value
    