class Item:
    def __init__(
                 self, 
                 name: str="", 
                 price: float=0, #why is not blocking receveing other data types?
                 quantity: int=0):
                
                assert price>=0, f'it looks like the item price is negative: {price}. it must be greater than 0.'
                assert quantity>=0, f'it looks like the item quantity is negative: {quantity}. it must be greater than 0.'

                self.name=name
                self.price=price
                self.quantity=quantity

    def total_price(self) -> float:
        return self.price*self.quantity

item1=Item('phone', 100, -5)
item1.has_numpad=False #this can be done yet even if __init__ exists
print(item1.total_price())

item2=Item('laptop', 5000, 3)
print(item2.total_price())

item3=Item()
print(item3.total_price())
