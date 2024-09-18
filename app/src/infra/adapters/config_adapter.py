import os

from app.src.domain.interfaces.adapters.config_adapter_interface import ConfigAdapterInterface


class ConfigAdapter(ConfigAdapterInterface):

    def get_usecase(self) -> str:
        return os.environ["USECASE"]