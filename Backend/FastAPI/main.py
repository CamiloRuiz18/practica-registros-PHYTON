from fastapi import FastAPI

app = FastAPI() #le asignamos la clase FastAPI a la variable

@app.get("/")
async def root():
    return "Hola mundo"