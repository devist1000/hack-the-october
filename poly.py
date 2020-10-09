class Flight:
    def __init__(self,engine):
        self.engine=engine
           
    def startEngine(self):
        self.engine.start(); #dependency injection
           
           
class Airbus:
    def start(self): 
        print("Engine start of Airbus")
         
class Boing:
    def start(self):
        print("Engine start for Boing") 
         
ae=Airbus()
f=Flight(ae)
f.startEngine()  

be=Boing()
f1=Flight(be)
f1.startEngine()  
