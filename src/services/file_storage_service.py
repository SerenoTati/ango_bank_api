


from abc import ABC, abstractmethod


class FileStorageService(ABC):
    """
        Abstract base class for file storage services.
        This class defines the interface for saving, deleting, and reading files.
        Concrete implementations can provide support for local or cloud storage.
    """  
    @abstractmethod
    def save(self, file_path: str, content: str) -> None:
        """
        Save a file to the storage.

        :param file_path: Path to the file to be saved.
        :param content: Content of the file to be saved.
        """
        pass
    @abstractmethod
    def delete(self, file_path: str) -> None:
        """
        Delete a file from the storage.

        :param file_path: Path to the file to be deleted.
        """
        pass
    @abstractmethod
    def read(self, file_path: str) -> str:
        """
        Read a file from the storage.
        :param file_path: Path to the file to be read.
        :return: Content of the file.
        """
        pass