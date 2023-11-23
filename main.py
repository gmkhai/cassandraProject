from fastapi import FastAPI
from api.products.apis import product_router


app = FastAPI()

app.include_router(product_router)
