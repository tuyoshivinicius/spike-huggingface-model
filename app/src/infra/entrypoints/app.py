from app.src.infra.adapters.config_adapter import ConfigAdapter
from app.src.infra.startups.catalog_model_startup import CatalogModelStartup
from app.src.infra.startups.classify_protection_startup import ClassifyProtectionStartup

class App:

    startup_strategies = {
        'classify_protection': ClassifyProtectionStartup,
        'catalog_model': CatalogModelStartup,
    }

    def run(self):
        config = ConfigAdapter()
        startup = self.startup_strategies[config.get_usecase()]()
        startup.run(config)










