from model.coche import Coche

class CocheRepository:
    coche_list = [
        Coche(id=1, marca="Ford", modelo="Focus", color="Rojo", precio=15000.0),
        Coche(id=2, marca="Renault", modelo="Clio", color="Azul", precio=12000.0),
        Coche(id=3, marca="Volkswagen", modelo="Golf", color="Blanco", precio=18000.0)
    ]

    @classmethod
    def get_all(cls):
        return cls.coche_list

    @classmethod
    def get_by_id(cls, id: int):
        return next((coche for coche in cls.coche_list if coche.id == id), None)

    @classmethod
    def add(cls, coche: Coche):
        cls.coche_list.append(coche)
        return coche

    @classmethod
    def update(cls, coche: Coche):
        for index, saved_coche in enumerate(cls.coche_list):
            if saved_coche.id == coche.id:
                cls.coche_list[index] = coche
                return coche
        return None

    @classmethod
    def delete(cls, id: int):
        for index, saved_coche in enumerate(cls.coche_list):
            if saved_coche.id == id:
                del cls.coche_list[index]
                return True
        return False