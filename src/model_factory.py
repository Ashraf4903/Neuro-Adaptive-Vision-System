from abc import ABC, abstractmethod
from src.utils import setup_logger

logger = setup_logger()

class BaseArchitecture(ABC):
    """
    Abstract base class enforcing a strict interface for all models.
    """
    @abstractmethod
    def build(self):
        pass

class NeuromorphicNet(BaseArchitecture):
    def __init__(self, config):
        self.layers = config.get('model', {}).get('layers', 3)
        self.type = config.get('model', {}).get('type', 'generic')

    def build(self):
        logger.info(f"🔨 Constructing {self.type} architecture...")
        logger.info(f"🔗 Initializing {self.layers} synaptic layers...")
        return f"Architecture<{self.type} | Layers: {self.layers}>"

class ModelBuilder:
    """
    Factory class to instantiate models based on configuration.
    """
    @staticmethod
    def get_model(config):
        model_type = config.get('model', {}).get('type')
        if "neuromorphic" in model_type:
            return NeuromorphicNet(config)
        else:
            raise ValueError(f"Unknown model type: {model_type}")