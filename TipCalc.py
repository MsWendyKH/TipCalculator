print("Tip Calculator by Wendy")
subtotal = float(input('SUBTOTAL: '))               # Total price of meal before tax and tip
quotient = subtotal / 100                           # Calculate 1% of the subtotal
tax = quotient * 10                                 # Multiply quotient * 10 to calculate sales tax
tax = round(tax, 2)                                 # Round to 2 decimal points to keep sums neat and tidy
print(f'TAX: ${tax}')                               # Displays tax to be added to the subtotal 
total = subtotal + tax                              # Subtotal plus tax = total bill before tip
total = round(total, 2)                             # Round to 2 decimal points to keep sums neat and tidy
print(f'TOTAL: ${total}')                           # Displays total price (Subtotal plus Tax)
tip = int(input('TIP%: '))                          # Input desired percentage of tip
guests = int(input('DIVIDE BY: '))                  # Divide the bill between.... 
sum = (float((tip / 100 +1) * subtotal) / guests)   # Calculate tip of subtotal and divide by guests 
payment = round(sum + tax / guests, 2)              # Add tax to tip and subtotal, divide by guests, round to 2 decimal points 
print(f'${payment}: Each')                          # Displays payment for each diner
