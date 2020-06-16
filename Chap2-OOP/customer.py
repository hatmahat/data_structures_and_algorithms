class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError('Invalid balance!')
        self._balance = new_bal

    # Add a decorator balance() method returning _balance
    @property  # read only property
    def balance(self):
        return self._balance

    # Add a setter balance() method 
    @balance.setter  # Able to set property
    def balance(self, new_bal):r
        # Validate the parameter value
        if new_bal < 0:
            raise ValueError('Invalid balance!')
        self._balance = new_bal
        print('Setter method called')

# Testing
cust = Customer('Belinda Lutz', 2000)

# Assign 3000 to the balance property
cust.balance = 3000

# Print the balance property
print(cust.balance)