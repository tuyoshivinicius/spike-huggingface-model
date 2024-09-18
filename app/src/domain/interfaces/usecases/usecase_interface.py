from abc import ABC, abstractmethod


class UseCaseInterface(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError