from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Pesquisa:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("start-maximized")
        
        self._driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        self._action = ActionChains(self._driver)
        self._wait = WebDriverWait(self._driver, 50)
        self._wait_quickly = WebDriverWait(self._driver,10)

    def get_url(self, url):
        self._driver.get(url)

    def search(self):
        try:
            pesquisar = self._wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')))
            pesquisar.click()

        except Exception as e:
            print(e)

        else:
            pesquisar.send_keys('euro')
            pesquisar.send_keys(Keys.RETURN)

    def get_euro(self):
        try:
            euro = self._wait_quickly.until(EC.presence_of_element_located((By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]')))
            print(f'1 Euro igual a: {euro.text}')
        except Exception as e:
            print(e)

    def clear_search(self):
        try:
            limpar = self._wait_quickly.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[3]/div[1]/div')))
            limpar.click()
        except Exception as e:
            print(e)

    def search_dollar(self):
        try:
            pesquisar = self._wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')))
            pesquisar.click()

        except Exception as e:
            print(e)

        else:
            pesquisar.send_keys('dolar')
            pesquisar.send_keys(Keys.RETURN)

    def get_dollar(self):
        try:
            dollar = self._wait_quickly.until(EC.presence_of_element_located((By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]')))
            print(f'1 Dollar igual a: {dollar.text}')
        except Exception as e:
            print(e)

       
    
def main():
    simples = Pesquisa()
    simples.get_url("https://www.google.com")
    time.sleep(1)
    simples.search()
    time.sleep(1)
    simples.get_euro()
    time.sleep(1)
    simples.clear_search()
    time.sleep(4)
    simples.search_dollar()
    time.sleep(1)
    simples.get_dollar()


main()