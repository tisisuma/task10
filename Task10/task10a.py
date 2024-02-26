from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class Task:
    def __init__(self, url):
        self.url = url

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except:
            print("ERROR : Unable to run the code !")
            return False

    def shutdown(self):
        self.driver.quit()

    def followers(self):
        try:
            sleep(3)
            followers_locator = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button/span/span"
            element = self.driver.find_element(by=By.XPATH, value=followers_locator)
            followerscount = element.text
            print("No of followers Count :" + followerscount)
        except NoSuchElementException as e:
            print("Error : ", e)

    def followingcount(self):
        try:
            sleep(3)
            following_locator = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span"
            element1 = self.driver.find_element(by=By.XPATH, value=following_locator)
            following = element1.text
            print("No of following Count :" + following)
        except NoSuchElementException as e:
            print("Error : ", e)


url = "https://www.instagram.com/guviofficial/"

execute = Task(url)
execute.booting_function()
execute.followers()
execute.followingcount()
execute.shutdown()
