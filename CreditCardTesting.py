import CreditCard as CC

"""
The Constructor
"""

cc = CC.CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)

print("Second Module's Name: {}".format(__name__))
print(cc.get_balance())
