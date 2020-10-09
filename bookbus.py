from threading import *

class BookMyBus:
    def __init__(self,availableseats):
        self.availableseats=availableseats
        self.l = Lock()  #lock show for thread syncronization ,also work for semaphore
        
    def buy(self,seatsrequired):
        self.l.acquire() 
        print("Total seats available:",self.availableseats)
        if self.availableseats>= seatsrequired:
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.availableseats -= seatsrequired
        else:
            print("SORRY!! No seats available")
        self.l.release()
        
bus=BookMyBus(12)
t1=Thread(target=bus.buy,args=(2,))
t2=Thread(target=bus.buy,args=(12,))
t3=Thread(target=bus.buy,args=(5,))

t1.start()
t2.start()
t3.start()
