from abc import ABC, abstractmethod


class ModelProviderAdapterInterface(ABC):

    @abstractmethod
    def save_to_storage(self):
        raise NotImplementedError

    @abstractmethod
    def load_from_storage(self):
        raise NotImplementedError
