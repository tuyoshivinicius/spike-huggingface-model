from abc import ABC, abstractmethod


class S3AdapterInterface(ABC):
    @abstractmethod
    def upload_file(self, file: str, bucket: str, key: str) -> None:
        pass

    @abstractmethod
    def download_file(self, bucket: str, key: str) -> str:
        pass