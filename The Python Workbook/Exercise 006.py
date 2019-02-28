meal_cost = float(input("How much was your meal? "))
tax = round(meal_cost * 0.13, 2)
tip = round(meal_cost * 0.18, 2)
total = round(meal_cost + tip + tax, 2)

print(f"""Tax is ${tax}
Tip is ${tip}
And the total is ${total}""")


