# import packages
# fastapi -> packages untuk membuat API
from fastapi import FastAPI, HTTPException
import pandas as pd

# FastAPI -> class untuk membuat API
app = FastAPI()

# api function -> get, put, post, delete

# membuat endpoint
# @object.function_api_type("url")
@app.get("/")
def home():
    return {"message": "Welcome, to HCK028!"}

# menjalankan API
# uvicorn nama_file_tanpa_py:nama_object --reload
# uvicorn main:app --reload

# membuat endpoint untuk membaca 
@app.get("/data")
def readData():
    # baca file
    df = pd.read_csv("dataToko.csv")
    # output
    return df.to_dict(orient="records")

@app.get("/data/{user_input}")
def searchData(user_input: int):
    # baca file
    df = pd.read_csv("dataToko.csv")
    
    #bikin filter
    filter = df[df["id"] == user_input]
    
    # bikin condition jika id barang tidak ada
    if len(filter) == 0:
        raise HTTPException(status_code=404, detail="Barangnya nggak ada bro :D")
    
    #output
    return filter.to_dict(orient="records")

# bikin endpoint untuk update data
@app.put("/item/{item_id}")
def updateData(item_id:int, item_name:str, item_price:int):
    # bara file yang sudah ada
    df = pd.read_csv("dataToko.csv")
    
    # data tambahan
    update_data = {"id": item_id, "namaBarang": item_name, "harga": item_price}
    
    #convert dict to df
    update_data_df = pd.DataFrame(update_data, index=[0])
    
    #menggabungkan data lama dengan data baru
    df = pd.concat([df, update_data_df], ignore_index = True)
    
    # simpan data ter-update
    df.to_csv("dataToko.csv", index=False)
    
    # outuput
    return {"message": f"item dengan nama {item_name} telah berhasil ditambahkan :D"}