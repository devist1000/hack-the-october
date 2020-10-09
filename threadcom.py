from threading import *;
from time import *;


class Producer:
    def __init__(self):
        self.product = []
        self.orderplaced = False
        
    def produce(self):
        for i in range(1,5):
            self.product.append("Product"+str(i))
            sleep(1.5)
            print("Item added")
        self.orderplaced=True
            
class Consumer:
    def __init__(self,prod):
        self.prod=prod
        
    def consume(self):
        while self.prod.orderplaced == False:
            print("order waiting awaits")
            sleep(0.2)
        
        print("Orders Shipped:",self.prod.product)
        
p=Producer()  
c=Consumer(p) 

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()
