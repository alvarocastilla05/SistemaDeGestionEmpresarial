from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI"

# Url local : http://127.0.0.1:8000

@app.get("/url")
async def url():
    return { "url_curso": "https://mouredev.com/pyhton"}


# Inicia el servidor: uvicorn main:app --reload
# Detener el servidor: CTRL+C

# Documentación de Swagger: http://127.0.0.1:8000/docs
# Documentación de Redocly: http://127.0.0.1:8000/redoc

