from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name: str
    description : str
    price : float
    quantity : int

    # Create a partial update model with all fields optional
class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    quantity: int | None = None

    # def __init__(self, id:int,name:str,description:str,price:float,quantity:int):
    #     self.id = id
    #     self.name = name
    #     self.discription = description
    #     self.price = price
    #     self.quantity = quantity