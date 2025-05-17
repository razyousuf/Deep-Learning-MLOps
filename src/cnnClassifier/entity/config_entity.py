from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration class for the Data Ingestion stage.
    This dataclass encapsulates all necessary paths and parameters required
    to perform data download and extraction.

    Attributes:
        root_dir (Path): Base directory for all data ingestion artifacts.
        source_URL (str): Google Drive shareable URL to the dataset zip file.
        local_data_file (Path): Path where the downloaded zip file will be saved.
        unzip_dir (Path): Directory where the zip file contents will be extracted.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
