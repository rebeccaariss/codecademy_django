train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#------------------------------------------------------------------------------------------------
# Write your code below:
#------------------------------------------------------------------------------------------------

# ✅ Convert Fahrenheit to Celsius:
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
# print(f100_in_celsius)


#------------------------------------------------------------------------------------------------


# ✅ Convert Celsius to Fahrenheit:
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
# print(c0_in_fahrenheit)


#------------------------------------------------------------------------------------------------


# ✅ Calculate total force for train:
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")


#------------------------------------------------------------------------------------------------


# ✅ Calculate total energy for bomb:
c = 3 * 10 ** 8 # c is a constant typically set to the speed of light

def get_energy(mass, c):
  return mass * (c ** 2)

bomb_energy = get_energy(bomb_mass, c)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


#------------------------------------------------------------------------------------------------


# ✅ Calculate work (defined as force multiplied by distance):
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + ".")
print(f"The GE train does {train_work} Joules of work over {train_distance}.")


#------------------------------------------------------------------------------------------------

# 💥 Physics project completed for Codecademy's "Learn Python 3" course:
# https://www.codecademy.com/learn/learn-python-3

#------------------------------------------------------------------------------------------------