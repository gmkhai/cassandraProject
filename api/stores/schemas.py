from pydantic import BaseModel
import decimal


class Store(BaseModel):
    store_name: str = str
    store_owner: str = str
    store_address: str = str
    store_lat: decimal = decimal
