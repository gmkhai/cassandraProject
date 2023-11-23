from pydantic import BaseModel


class Product(BaseModel):
    product_name: str = str
    product_category: str = str
    product_quantity: int = 0
    product_description: str = str
    product_store: str = str


class Category(BaseModel):
    category_name: str = str
    category_code: str = str


class ProductByCategory(BaseModel):
    category_name: str = str
    product_description: str = str
    product_name: str = str
