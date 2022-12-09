from fastapi import FastAPI
from router import var1

app = FastAPI()
app.include_router(var1)




