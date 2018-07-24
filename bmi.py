
def calculate_bmi(height,weight):
    square_height = height*height
    result = weight/ square_height
    return result
height = input("height(metry) : ")
weight = input("weight(kg) : ")
    
print calculate_bmi(height,weight)
