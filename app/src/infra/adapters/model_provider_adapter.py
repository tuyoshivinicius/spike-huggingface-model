import os

from sentence_transformers import SentenceTransformer

from app.src.domain.interfaces.adapters.model_provider_adapter_interface import ModelProviderAdapterInterface
from app.src.domain.interfaces.adapters.s3_adapter_interface import S3AdapterInterface


class ModelProviderAdapter(ModelProviderAdapterInterface):

    def __init__(self, s3_adapter: S3AdapterInterface):
        self.s3_adapter = s3_adapter

    def save_to_storage(self):
        current_directory = os.getcwd()
        model_path = f"{current_directory}/data"
        model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
        model.save(model_path)

        # TODO: zipar e fazer upload para o s3

    def load_from_storage(self):

        current_directory = os.getcwd()
        model_path = f"{current_directory}/data"

        # TODO: fazer download do s3 e colocar em model_path

