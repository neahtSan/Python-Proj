def simple_velocity_calculator(distance, time):
    velocity = distance / time
    return velocity
distance = input("distance(metre) : ")
time = input("time(second) : ")
print simple_velocity_calculator(distance, time), "m/s"
