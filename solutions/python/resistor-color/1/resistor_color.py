def color_code(color):
    """This function gives the resistor value of a color"""
    color_panel = colors()
    
    if color in color_panel:
        return color_panel.index(color)


def colors():
    """This function holds the resistor color library"""
    return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
