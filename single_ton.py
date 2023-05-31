

def singleton(func):
    d={}
    def inner():
        if func not in d:
            d[func]=func()
        return d[func]
    return inner


@singleton           ## Multiplex=singleton(Multiplex)
class Multiplex:
    def __init__(self):
        self.tickets=300

    def booking(self,n):
        if self.tickets>=n:
            self.tickets-=n
            print("Ticket Booked")
        else:
            print("Sold out")

tushar=Multiplex()
tushar.booking(200)
print(tushar.tickets)#100
print(tushar)
tushar.booking(100)
print(tushar.tickets)#0

arnab=Multiplex()
arnab.booking(200)
print(arnab.tickets)
print(arnab)




