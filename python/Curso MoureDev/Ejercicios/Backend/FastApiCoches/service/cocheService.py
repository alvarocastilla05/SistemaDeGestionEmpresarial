from model.coche import Coche
from repository.cocheRepository import CocheRepository

class CocheService:
    @staticmethod
    def get_coches():
        return CocheRepository.get_all()

    @staticmethod
    def get_coche_by_id(id: int):
        return CocheRepository.get_by_id(id)

    @staticmethod
    def create_coche(coche: Coche):
        if CocheRepository.get_by_id(coche.id):
            return None
        return CocheRepository.add(coche)

    @staticmethod
    def update_coche(coche: Coche):
        return CocheRepository.update(coche)

    @staticmethod
    def delete_coche(id: int):
        return CocheRepository.delete(id)