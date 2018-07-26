print("=========== CALCULATOR ============")
print("1.Straight line in motion \n2.Projectile")

def motion():
    print "1.No acceleration \n2.With acceleration "
    user_choice = input("Select 1 or 2 for your choice: ")
    if(user_choice == 1):
        distance = input("distance(metre) : ")
        time = input("time(second) : ")
        velocity = distance / time
        return velocity
    
    

while(True):
   choice = input("select your choice: ")
   if(choice == 1):
       velocity = motion()
       print("Velocity = " + str(velocity) +" m/s")
        