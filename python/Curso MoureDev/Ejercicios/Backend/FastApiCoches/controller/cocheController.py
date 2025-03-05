from fastapi import APIRouter, HTTPException
from model.coche import Coche
from service.cocheService import CocheService
router = APIRouter()

@router.get("/coches")
async def get_coches():
    return CocheService.get_coches()

@router.get("/coche/{id}")
async def get_coche(id: int):
    coche = CocheService.get_coche_by_id(id)
    if not coche:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    return coche

@router.post("/coche/", response_model=Coche, status_code=201)
async def create_coche(coche: Coche):
    new_coche = CocheService.create_coche(coche)
    if not new_coche:
        raise HTTPException(status_code=400, detail="El coche ya existe")
    return new_coche

@router.put("/coche/")
async def update_coche(coche: Coche):
    updated_coche = CocheService.update_coche(coche)
    if not updated_coche:
        raise HTTPException(status_code=400, detail="No se pudo actualizar el coche")
    return updated_coche

@router.delete("/coche/{id}")
async def delete_coche(id: int):
    if not CocheService.delete_coche(id):
        raise HTTPException(status_code=400, detail="No se pudo eliminar el coche")
    return {"message": "Coche eliminado"}
