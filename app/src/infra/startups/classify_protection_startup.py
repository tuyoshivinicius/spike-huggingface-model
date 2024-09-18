from flask import Flask, jsonify
from app.src.application.usecases.classify_protection_usecase import ClassifyProtectionUseCase
from app.src.domain.interfaces.adapters.config_adapter_interface import ConfigAdapterInterface
from app.src.domain.interfaces.startup.startup_strategy_interface import StartupStrategyInterface
from app.src.infra.startups.threads.usecase_thread import UseCaseThread


class ClassifyProtectionStartup(StartupStrategyInterface):

    def run(self, config: ConfigAdapterInterface):

        usecase = ClassifyProtectionUseCase()

        thread = UseCaseThread(usecase)
        thread.start()

        app = Flask(__name__)

        @app.route("/healthcheck", methods=["GET"])
        def health():
            if thread.is_running():
                return jsonify({"status": "UP"}), 200
            else:
                return jsonify({"status": "DOWN"}), 404

        app.run(host='0.0.0.0', port=5000)







