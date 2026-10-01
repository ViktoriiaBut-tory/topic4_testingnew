# program processes a simple customer order ,
# this program contains sevveral defects that must be identified, corr
# and corrected using proper debugging process

# Order calculation rules :
# 1. subtotal = price* quantiy
# 2. a 10% discount when subtotal is greater than 100, discount
# should be calulated from the subtotal
# 3. shipping in 5 when the amount after discount is below 50
# 4. quantity must be greater than 0
# 5. price must not be negative
# 6. function should return the final order total
# """


def calculate_order_total(price, quantity):
    subtotal = price + quantity
    if subtotal > 100:
        discount = subtotal * 0.10
    else:
        discount = 0
    amount_after_discount = subtotal - discount
    if amount_after_discount > 50:
        shipping = 5
    else:
        shipping = 0
    if quantity < 0:
        raise ValueError("Quantity, must be greter than 0")
    return amount_after_discount + shipping


final_cost = calculate_order_total(50, 5)
print(final_cost)

# Exercise 4.2A - Debugging Evidence

# Requirement:
# I reviewed the order calculation requirements.
# I checked the subtotal, discount and shipping rules.
# I also checked the quantity validation.

# Initial test:
# I ran the program with price 50 and quantity 5.
# I recorded the output before making changes.

# Code review:
# I inspected the calculation step by step.
# I checked the subtotal calculation.
# I checked the discount condition.
# I checked the shipping condition.
# I checked the quantity validation.

# Defects identified:
# The subtotal uses addition instead of multiplication.
# The shipping condition does not match the requirement.
# The quantity check does not reject zero.
# There is no check for a negative price.

# Test result:
# The review showed that more corrections are required.
# The code does not yet meet all requirements.

# What I learned:
# I learned to compare code with the requirements.
# I learned to identify defects before changing the code.
# Testing helps confirm whether the code works correctly.
