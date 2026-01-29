#create class
class Vechile:

  #create innit method
    def __init__(self,max_speed,mileage):
    #bind the arguments
       self.max_speed=max_speed
       self.mileage=mileage
#object creation
modelX=Vechile(240,18)
#acess the variables inside innit method
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:",modelX.mileage)
