import pandas as pd
from imblearn.over_sampling import SMOTE


def resample_with_smote(data: pd.DataFrame) -> pd.DataFrame:
    smote = SMOTE(sampling_strategy="minority")
    X, y = smote.fit_resample(data.drop("class", axis=1), data["class"])
    X["class"] = y
    return X
