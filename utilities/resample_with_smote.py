import pandas as pd
from imblearn.over_sampling import SMOTE


def resample_with_smote(
    data: pd.DataFrame, random_state=None, sampling_strategy: str | float = 0.5
) -> pd.DataFrame:
    smote = SMOTE(sampling_strategy=sampling_strategy, random_state=random_state)
    X, y = smote.fit_resample(data.drop("class", axis=1), data["class"])
    X["class"] = y
    return X
