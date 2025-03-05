from fastapi import FastAPI
from controller.cocheController import router as coche_router

app = FastAPI()

app.include_router(coche_router)

from pydantic import BaseModel