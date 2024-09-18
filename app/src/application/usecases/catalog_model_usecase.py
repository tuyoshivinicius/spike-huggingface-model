from app.src.domain.interfaces.adapters.model_provider_adapter_interface import ModelProviderAdapterInterface
from app.src.domain.interfaces.usecases.usecase_interface import UseCaseInterface


class CatalogModelUseCase(UseCaseInterface):

    def __init__(self, model_provider_adapter: ModelProviderAdapterInterface):
        self.model_provider_adapter = model_provider_adapter

    def execute(self):
        self.model_provider_adapter.save_to_storage()