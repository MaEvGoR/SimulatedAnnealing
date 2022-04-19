import pandas as pd
import json

from urllib.request import urlopen


class Data():

    def __init__(self):
        self.df = None
        self.setup()

    def setup(self):
        self.upload_cities()

    def upload_cities(self):
        raw_df = pd.read_csv('src/data/raw/city.csv')
        self.df = raw_df.loc[raw_df['population'].nlargest(30).index]

    def get_data(self):
        return self.df


data = Data()
