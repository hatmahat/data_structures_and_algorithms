class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
        # Recall that Python allows multiple varible assignments in one line
        self.year, self.month, self.day = year, month, day

    # Define a class method from_ste
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)

# TEST
bd = BetterDate.from_str('2020-04-30')
print(bd.year)
print(bd.month)
print(bd.day)