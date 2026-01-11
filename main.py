import sys
import yaml
import argparse
from src.data_loader import DataLoader
from src.model_factory import ModelBuilder
from src.trainer import Trainer
from src.utils import setup_logger

# Initialize Logger
logger = setup_logger()

def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logger.error(f"❌ Configuration file not found at {config_path}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Run Neuro-Adaptive Architecture Prototype")
    parser.add_argument('--config', type=str, default='configs/model_config.yaml', help='Path to config file')
    args = parser.parse_args()

    logger.info("========================================")
    logger.info("   NEURO-ADAPTIVE VISION SYSTEM v0.1    ")
    logger.info("========================================")

    # 1. Load Configuration
    config = load_config(args.config)
    logger.info("✅ Configuration loaded successfully.")

    # 2. Initialize Data Pipeline
    loader = DataLoader(config)
    data = loader.load_data()

    # 3. Build Model Architecture
    model_container = ModelBuilder.get_model(config)
    architecture = model_container.build()
    
    # 4. Initialize Trainer
    trainer = Trainer(architecture, config)
    trainer.start_training()

    logger.info("========================================")
    logger.info("🎉 STRUCTURAL VERIFICATION SUCCESSFUL")
    logger.info("========================================")

if __name__ == "__main__":
    main()