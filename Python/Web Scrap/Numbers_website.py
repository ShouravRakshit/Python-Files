from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
website = "https://www.the-numbers.com/movie/budgets"
tim = "https://tech-with-tim.teachable.com/p/the-fundamentals-of-programming-with-python"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(website)
time.sleep(10)

