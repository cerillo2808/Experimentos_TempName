from pydoc import describe

import data.loader as loader

df = loader.get_data()

describe(df.head())