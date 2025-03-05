from pydantic import BaseModel

class Coche(BaseModel):
    id: int
    marca: str
    modelo: str
    color: str
    precio: float