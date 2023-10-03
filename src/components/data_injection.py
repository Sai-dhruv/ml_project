import os
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import pandas as pd

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataInjection:
    def __init__(self):
        self.injection_config = DataIngestionConfig()

    def initiate_data_injection(self):
        logging.info("Entered into initiate data injection method")
        try:
            data_file_path = 'P:\\ml_projects\\notebook\\data\\stud.csv'
            df = pd.read_csv(data_file_path)
            logging.info("Exported dataset dataFrame..")
            os.makedirs(os.path.dirname(self.injection_config.train_data_path), exist_ok=True)
            df.to_csv(self.injection_config.raw_data_path, index=False, header=True)
            logging.info("Train Test split initiated ...!")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.injection_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.injection_config.test_data_path, index=False, header=True)
            logging.info("Injection of the data completed ...")


            return (
                self.injection_config.train_data_path,
                self.injection_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)




if __name__ == "__main__":
    obj = DataInjection()
    obj.initiate_data_injection()