import csv
import os
from services.Util import Util

class CSV(Util):
    def __init__(self) -> None:
        self.__dirName = f"./files"
        self.__check_dir_exists()

    def __check_dir_exists(self) -> None:
        if not os.path.isdir(self.__dirName):
            os.mkdir(self.__dirName)

    def __get_headers(self, data: list) -> dict:
        return data[0].keys()        

    def save(self, prefix: str, data: list) -> None:
        try:
            with open(f"{self.__dirName}/{prefix}-{self.date_time()}.csv", 'w', newline='', encoding='utf-8') as file:
                
                writer = csv.writer(file)
                writer.writerow(self.__get_headers(data))
                
                for i in data:
                    writer.writerow(i.values())
                        
                file.close()
                
        except IOError as e:
            raise IOError(f"Ocorreu um erro ao salvar o conteúdo no arquivo CSV: {e}")
