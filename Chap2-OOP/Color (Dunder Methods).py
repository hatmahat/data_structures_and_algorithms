class Color:
    def __init__(self, red, blue, green):
        self.red, self.blue, self.green = red, blue, green

    def __repr__(self):
        return 'Color with RGB = ({}, {}, {})'.format(
            self.red, self.blue, self.green
        )
    
    def __add__(self, other):
        """
        Adds two RGB colors together
        Maximum value is 255
        """

        new_red = min(self.red + other.red, 255)
        new_blue = min(self.blue + other.blue, 255)
        new_green = min(self.green + other.green, 255)

        return Color(new_red, new_blue, new_green)

red = Color(255, 0, 0)
print('red      :', red)
blue = Color(0, 255, 0)
print('blue     :', blue)
green = Color(0, 0, 255)
print('green    :', green)

magenta = red + blue
print('magenta  :', magenta)

cyan = blue + green
print('cyan     :', cyan)

yellow = red + green
print('yellow   :', yellow)

white = red + green + blue
print('white    :', white)