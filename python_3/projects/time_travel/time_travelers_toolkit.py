import datetime as dt
from decimal import Decimal
from random import randint, choice # note use of comma here
import custom_module

destinations = ['Canada', 'Mexico', 'China', 'India', 'Germany', 'France', 'Russia', 'Korea', 'Japan', 'Indonesia', 'Egypt', 'Somalia', 'Greece', 'Turkey', 'Italy', 'Colombia', 'Brazil', 'Chile', 'Portugal', 'Uruguay', 'Spain', 'Iran', 'Ireland', 'Scotland', 'Nepal', 'Somalia', 'Namibia', 'Greenland', 'Iceland']

current_date = dt.date.today()
current_time = dt.datetime.now().time()
current_year = dt.date.today().year
random_year = randint(1000, 3025)
base_cost = Decimal('3000.00')
random_destination = choice(destinations)

# Calculate cost multiplier based on the difference in years:
cost_multiplier = abs(current_year - random_year)
total_cost = (base_cost + Decimal("100") * Decimal(cost_multiplier)).quantize(Decimal('0.00'))

print(f"The current date is: {current_date.strftime('%A, %B %d, %Y')}.")
print(f"The current time is: {current_time.strftime('%H:%M %p')}.") # => '%p' results in 'AM', 'PM'; '%P' results im 'am', 'pm'

message = custom_module.generate_time_travel_message(random_destination, random_year, total_cost) # Positional function arguments
# Can also call with keyword arguments:
# message = custom_module.generate_time_travel_message(year=random_year, destination=random_destination, cost=total_cost)

print(message)

#------------------------------------------------------------------------------------------------

# 🚀 "Time Traveler's Toolkit" project completed for Codecademy's "Learn Python 3" course:
# https://www.codecademy.com/learn/learn-python-3

#------------------------------------------------------------------------------------------------