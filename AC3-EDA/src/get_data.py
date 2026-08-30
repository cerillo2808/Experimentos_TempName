import os
from pathlib import Path
import os
import kagglehub
import pandas as pd
from functools import cache


def get_cache_dir() -> Path:
    """
    Returns the path to the custom cache directory for kagglehub.
    The cache directory is set to a folder named 'data/raw' in the project root.

    Returns:
        Path: The path to the cache directory.
    """
    PROJECT_ROOT = Path(__file__).resolve().parent.parent  # Adjust depth as needed
    CACHE_DIR = PROJECT_ROOT / "data" / "raw"
    os.environ["KAGGLEHUB_CACHE"] = str(CACHE_DIR)

    return CACHE_DIR

@cache
def get_data() -> pd.DataFrame:
    """
    Downloads (if needed) the dataset from Kaggle using kagglehub and loads it into a pandas DataFrame.

    Returns:
        pd.DataFrame: The loaded dataset.
    """
    # use the custom cache directory for kagglehub and print the cache directory path
    print("Cache directory:", get_cache_dir())

    # download the dataset from Kaggle using kagglehub
    data_path = kagglehub.dataset_download("debayank2024/house-price-prediction")
    file_path = os.path.join(data_path, "modified_data.csv")

    # load locally using pandas
    df = pd.read_csv(file_path)

    # display the first few records of the dataset
    print("Path to file:", file_path)
    print("First 5 records:\n", df.head())

    return df


get_data()