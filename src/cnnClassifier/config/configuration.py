# 3. Configuration Manager
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    """
    Manages the retrieval and setup of configuration objects required for different pipeline components.
    Loads configurations from YAML files and ensures required directories are created.
    """

    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        """
        Initializes the ConfigurationManager.

        Args:
            config_filepath (str): Path to the main config YAML file.
            params_filepath (str): Path to the parameters YAML file.
        """
        # Load YAML configuration files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Ensure the global artifacts root directory exists
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Constructs the configuration for the data ingestion stage.

        Returns:
            DataIngestionConfig: A data class containing all configuration values
            needed by the DataIngestion component.
        """
        # Extract data ingestion config section
        config = self.config.data_ingestion

        # Ensure the root directory for data ingestion exists
        create_directories([config.root_dir])

        # Package values into a structured DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
