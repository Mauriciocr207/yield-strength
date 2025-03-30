import pandas as pd
import os

class DataManager:
    def __init__(self, files: list[str]):
        self.files = files

    def load_data(self, columns: list[str] = None):
        data = []
        for file in self.files:
            filepath = f"./data/{file}";
            df = pd.read_excel(filepath, usecols=columns)
            data.append(df)
        return data
        
