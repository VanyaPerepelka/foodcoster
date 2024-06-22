import pandas as pd


def to_csv(dictionary, file_name):
    frame = pd.DataFrame.from_dict(dictionary, orient="index",)
    frame.to_csv(file_name)
