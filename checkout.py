# This is a Python program to total a checkout price for grocery items

apple = .79
banana = .89
strawberries = 3.49
celery = 1.29

convenience_fee = 2.00

tax = (apple + banana + strawberries + celery) * .06

total = tax + convenience_fee + (apple + banana + strawberries + celery)

print(f"Your total for today is ${total:.2f}, including tax.")