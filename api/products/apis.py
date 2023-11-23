import pandas as pd
from typing import Annotated
from fastapi import APIRouter, status, UploadFile, File
from configs import product_session, clusters

product_router = APIRouter()


@product_router.post('/product_upload')
async def product_upload(file: Annotated[UploadFile, File(description="A file read as UploadFile")]):
    """
    save data file to cassandra database
    :param file:
    :return:
    """
    contents = await file.read()
    data_frame = pd.read_excel(contents)

    # select feature for save to cassandra database
    data = data_frame[['InvoiceNo', 'Description', 'Country']]
    data['InvoiceNo'] = data['InvoiceNo'].astype('str')

    # drop missing data
    data.dropna(axis=0, subset=['InvoiceNo', 'Description', 'Country'], inplace=True)

    # iteration rows data
    for index, row in data.iterrows():
        invoice_id = row['InvoiceNo']
        description = row['Description']
        country = row['Country']

        # Use parameter binding (?) for forbidden SQL injection access
        query = "INSERT INTO product_by_invoiceid (invoice_id, country, product_description) VALUES (%s, %s, %s)"
        product_session.execute(query, (invoice_id, country, description))

    clusters.shutdown()

    response = {
        "message": "Upload file" + file.filename + " berhasil"
    }
    return response


@product_router.get('/product-list')
def product_list():
    response = {
        "status": status.HTTP_200_OK
    }
    return response
