import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        Load a csv file in a dataframe.
        Can raise Exceptions.
    """
    df = pd.read_csv(path)
    print('Loading dataset of dimensions', df.shape)
    return df
