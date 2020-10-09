class BMW:
    def __init__(self,make,model,year):
        self.model=model
        self.make=make
        self.year=year
        
    def start(self):
        print("Start the car")
        
    def stop(self):
        print("Stop the car")
    

        
class Threeseries(BMW):
    def __init__(self,cruisedcontrol,make,model,year):
        super().__init__(make,model,year) # inplace of the parent class name that is BMW and while changing it remove self
        self.cruisedcontrol=cruisedcontrol
        
    def start(self):
        print("button start")
    def display(self):
        print(self.cruisedcontrol)
        
class fiveseries(BMW):
    def __init__(self,parkingassistant,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingassistant=parkingassistant
        
threeseries=Threeseries(True,"BMW","0345",2019)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)

threeseries.start()
threeseries.stop()

threeseries.display()

Fiveseries = fiveseries(True,"BMW","5674",2020)
print(Fiveseries.parkingassistant)
print(Fiveseries.make)
print(Fiveseries.model)
print(Fiveseries.year)

Fiveseries.start()
Fiveseries.stop()
