import matplotlib.pyplot as plt
import pandas as pd
from typing import List


def draw_bar_class_value_counts(datasets: List[pd.DataFrame], titles: List[str]):
    fig, axs = plt.subplots(1, len(datasets), figsize=(15, 5))
    for i, data in enumerate(datasets):
        data["class"].value_counts().plot(kind="bar", ax=axs[i])
        axs[i].set_title(titles[i])
        axs[i].set_xlabel("Class")
        axs[i].set_ylabel("Count")
    plt.show()
