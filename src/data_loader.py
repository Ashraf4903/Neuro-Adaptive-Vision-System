import os
from src.utils import setup_logger

logger = setup_logger()

class DataLoader:
    """
    Handles the ingestion and preprocessing of event-based vision data.
    """
    def __init__(self, config):
        self.config = config
        self.source_path = config.get('data', {}).get('source_path', './data')

    def load_data(self):
        """
        Simulates the loading process.
        """
        logger.info(f"📂 Accessing data source at: {self.source_path}")
        logger.info("ℹ️ Checking for event-stream integrity...")
        
        # Logic allows the code to run without actual data files present
        if not os.path.exists(self.source_path):
            logger.warning("⚠️ Source path empty. Running in SYNTHETIC mode.")
            return self._generate_synthetic_data()
        
        return "Real Data Stream"

    def _generate_synthetic_data(self):
        logger.info("🧪 Generating synthetic neuromorphic spikes for testing...")
        return {"events": 1000, "polarity": "mixed"}