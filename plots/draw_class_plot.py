import matplotlib.pyplot as plt
import pandas as pd


def draw_class_plot(data: pd.DataFrame, title: str, is_subplot=False, subplot_index=0):
    if is_subplot:
        plt.subplot(1, 3, 1 + subplot_index)

    data["class"].value_counts().plot(kind="bar")
    plt.title(title)
    plt.xlabel("Class")
    plt.ylabel("Count")
