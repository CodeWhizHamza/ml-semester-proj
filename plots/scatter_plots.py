import matplotlib.pyplot as plt
import pandas as pd
from typing import List


def draw_scatter_subplots(datasets: List[pd.DataFrame], titles: List[str]):
    fig, axs = plt.subplots(1, len(datasets), figsize=(15, 5))
    for i, data in enumerate(datasets):
        axs[i].scatter(
            data.iloc[:, 0],
            data.iloc[:, 1],
            c=data["class"].map({"cotton": 0, "rice": 1}),
            cmap="viridis",
            alpha=0.5,
        )
        axs[i].set_title(titles[i])
        axs[i].set_xlabel("X")
        axs[i].set_ylabel("Y")
    plt.show()
