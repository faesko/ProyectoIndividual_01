from fastapi import FastAPI
#from router import var1

app = FastAPI()

#@app.get("/")
#async def root():
#    return {"message": "Hello World"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cosas/{cosas_id}")
def read_item(item_id: int, q: str = None):
    return {"item_ide": item_id, "CU": q}

#app.include_router(var1)




