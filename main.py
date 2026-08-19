from fastapi import FastAPI,Depends,HTTPException
from model import Product ,ProductUpdate
from db.database import session,engine
import database_models
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from user_models import User

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers =["*"]
)

database_models.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

def get_db():
    db= session()
    try:
        yield db
    finally:
        db.close()

def init_db ():
    db = session()
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
            db.commit()
init_db()


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

@app.get("/products/")
def get_all_products(db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def product_by_id(id:int,db:Session=Depends(get_db)):
        # for prod in range(len(products)):
    #     if  products[prod].id == id:
    #         return products[prod]
    
    # for prod in products:
    #     if prod.id == id:
    #         return prod
    # else :
    #     return "Unable to Reach :("
    db_product = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
    return "not found so far "


# @app.post("/")
# def add_product(id,name,disc,price,quantity):
#     Products.id = id 
#     Products.name = name
#     Products.discription = disc
#     Products.price = price
#     Products.quantity = quantity

#     for index,product in Products:
#         if product[index] == Products.id :
#             current_product = product
#             return current_product 

@app.post("/products/")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.patch("/products/{id}")
def update_product_partial(id: int,product_update: ProductUpdate,db: Session = Depends(get_db)):
    # Get the product from database
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product NOT Found")
    # Update only the fields that were provided
    update_data = product_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
    
    db.commit()
    db.refresh(db_product)  # Refresh to get updated data
    return db_product

@app.put("/products/{id}")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_product= db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return db_product
    else :
        return "Product NOT Found"

    # for index in range(len(products)):
    #     if products[index].id == id:
    #         products[index] = product
    #         print(product)
    #         return product
    return 'unable to update product :('


@app.delete('/products/{id}')
def delete_product(id:int,db:Session=Depends(get_db)):
    db_product= db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:    
        db.delete(db_product)
        db.commit()
    else:
        return "product not found"
    # for i in range(len(products)):
    #     if products[i].id ==id:
    #         del products[i]
    #         return {'message':'product deleted'} 

    # '''for prod in products:
    #     if prod.id == id:
    #         #my logic 
    #         print(prod) 
    #         del products[id-1]
    #         for p in products:
    #             print(p)'''
            
    # return {'message':'product not found :( '}
    