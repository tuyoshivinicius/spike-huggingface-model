from app.src.application.usecases.catalog_model_usecase import CatalogModelUseCase
from app.src.domain.interfaces.adapters.config_adapter_interface import ConfigAdapterInterface
from app.src.domain.interfaces.startup.startup_strategy_interface import StartupStrategyInterface
from app.src.infra.adapters.model_provider_adapter import ModelProviderAdapter


class CatalogModelStartup(StartupStrategyInterface):

    def run(self, config: ConfigAdapterInterface):

        model_provider_adapter = ModelProviderAdapter()

        usecase = CatalogModelUseCase(
            model_provider_adapter=model_provider_adapter
        )
        usecase.execute()
        a=1