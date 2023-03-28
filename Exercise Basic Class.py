#Write a Python class,

#MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.

#Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type

#If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class


class MedPlus:
    def __init__(self, name: str, batch_number: int, price: float):
        self.name = name
        self.batch_number = batch_number
        self.price = price
        
    def set_name(self, name: str):
        self.name = name
        
    def set_batch_number(self, batch_number: int):
        self.batch_number = batch_number
        
    def set_price(self, price: float):
        self.price = price
    
    def get_name(self) -> str:
        return self.name
    
    def get_batch_number(self) -> int:
        return self.batch_number
    
    def get_price(self) -> float:
        return self.price

medicine = MedPlus("DP Gesic", 25, 14.22)
print(medicine.get_name())
medicine.set_price(52.5)
print(medicine.get_price())
