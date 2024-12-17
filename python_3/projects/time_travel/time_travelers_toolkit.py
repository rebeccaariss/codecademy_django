import datetime as dt
from decimal import Decimal
from random import randint, choice # note use of comma here
import custom_module

date = dt.date.today()
time = dt.datetime.now().time()

print(date.strftime('%A, %B %d, %Y'))
print(time.strftime('%H:%M %P')) # => pm
print(time.strftime('%H:%M %p')) # => PM

base_cost = Decimal('3000.00')
print(base_cost)
