#for simple calculate only
def simple_acceleration_caculator(initial_v, final_v, time):
    delta_v = final_v - initial_v
    acceleration = delta_v / time
    return acceleration
#to get information
initial_v = input("initial v(m/s) : ") 
final_v = input("final v(m/s) : ")
time = input("time(s) : ")

print simple_acceleration_caculator(initial_v, final_v, time) , "metre per second square"
