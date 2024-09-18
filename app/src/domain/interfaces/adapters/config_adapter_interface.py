from abc import abstractmethod


class ConfigAdapterInterface:

    @abstractmethod
    def get_usecase(self) -> str:
        raise NotImplementedError