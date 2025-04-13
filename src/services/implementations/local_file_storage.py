
import os

from services.file_storage_service import FileStorageService


class LocalFileStorage(FileStorageService):

    def save(self, file_path: str, content: str) -> None:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            file.write(content)

    def delete(self, file_path: str) -> None:
        if os.path.exists(file_path):
            os.remove(file_path)

    def read(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        with open(file_path, 'r') as file:
            return file.read()