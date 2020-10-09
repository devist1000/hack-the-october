class car:
    def __init__(self,year,make):
        self.make=make
        self.year=year
        
    class engine:
        def __init__(self,number):
            self.num=number
        def start(self):
            print("engine started")    
c=car(2020,"BMW")

e=c.engine(345)
e.start()
