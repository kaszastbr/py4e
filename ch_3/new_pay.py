rate = float(input('Hourly rate, please\n'))
hours = float(input('How many hours have you worked for?\n'))
if hours <= 40:
    payment = rate * hours
else:
    payment = (rate * 40) + (1.5 * rate * (hours - 40))
# payment = round(rate * hours,2)
print('Your gross pay will be', payment)