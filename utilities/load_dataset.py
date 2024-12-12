import pandas as pd


def load_cotton(file_path: str) -> pd.DataFrame:
    data = pd.read_csv(file_path)
    data["class"] = "cotton"
    return data


def load_rice(file_path: str) -> pd.DataFrame:
    data = pd.read_csv(file_path)
    data["class"] = "rice"
    return data
