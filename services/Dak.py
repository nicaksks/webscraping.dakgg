from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from services.Util import Util
from services.Csv import CSV

class Dak(Util):
    def __init__(self) -> None:
        super().__init__()
        
        # Navegador;
        self._browser = webdriver.Chrome()
        
        # Opções do navegador;
        self._browser.maximize_window()
        
        # Csv
        self._csv = CSV()

    def wait(self, xpath: str, time: int = 30):
        return WebDriverWait(self._browser, time).until(self.__find_Element(xpath))

    def __find_Element(self, xpath: str):
        return EC.presence_of_element_located((By.XPATH, xpath))

    def exit(self) -> None:
        self._browser.quit()
