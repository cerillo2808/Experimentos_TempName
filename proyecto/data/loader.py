import decimal

import pandas as pd
from pathlib import Path
import glob


def get_data() -> pd.DataFrame:
    """
    Reads the dataset from the downloaded CSV file and loads it into a pandas DataFrame.

    Returns:
        pd.DataFrame: The loaded dataset.
    """
    # files = glob.glob(os.path.join(data.get_cache_dir(), "*.csv"))

    DATA_DIR = Path(__file__).parent

    df = pd.concat(
        [pd.read_csv(file, decimal=",") for file in glob.glob(str(DATA_DIR / "*.csv"))],
        ignore_index=True,
    )
    df["Lectura del sensor (mm)"] = df["Lectura del sensor (cm)"].astype(float) * 10 # convertir a mm
    df["Distancia de referencia (mm)"] = df["Distancia de referencia (cm)"].astype(float) * 10 # convertir a mm
    df["Error con signo (mm)"] = df["Error con signo (cm)"].astype(float) * 10 # convertir a mm
    df["Error absoluto (mm)"] = df["Error absoluto (cm)"].astype(float) * 10 # convertir a mm
    # df["Error relativo (%)"] = df["Error relativo (%)"].astype(float) # convertir a float

    # display the first few records of the dataset
    print("Dataset information:")
    for i, file in enumerate(glob.glob(str(DATA_DIR / "*.csv"))):
        print(f"\tPath to file {i + 1}: \'{file}\'")
    print("\tFirst 5 records:\n", df.head())

    return df


