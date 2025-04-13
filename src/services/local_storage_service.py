from abc import ABC

from models.dto import DTO

class LocalStorageService(ABC):

    def save(dto:DTO) -> None:
        pass
    def delete(id: int) ->None:
        pass
    def update(dto:DTO) -> None:
        pass
    def get(id:int)->DTO:
        pass
