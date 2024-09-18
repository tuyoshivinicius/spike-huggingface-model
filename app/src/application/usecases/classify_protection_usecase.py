import time

from app.src.domain.interfaces.adapters.model_provider_adapter_interface import ModelProviderAdapterInterface
from app.src.domain.interfaces.usecases.usecase_interface import UseCaseInterface


class ClassifyProtectionUseCase(UseCaseInterface):

    def __init__(self, model_provider_adapter: ModelProviderAdapterInterface):
        self.model_provider_adapter = model_provider_adapter

        # carregando modelo do s3 para o container
        self.model_provider_adapter.load_from_storage()

    def execute(self):
        print("ClassifyProtectionUseCase executed")
        time.sleep(60)
