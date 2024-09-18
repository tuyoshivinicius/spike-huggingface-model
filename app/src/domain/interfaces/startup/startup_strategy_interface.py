from abc import abstractmethod, ABC

from app.src.domain.interfaces.adapters.config_adapter_interface import ConfigAdapterInterface


class StartupStrategyInterface(ABC):

    @abstractmethod
    def run(self, config: ConfigAdapterInterface):
        raise NotImplementedError