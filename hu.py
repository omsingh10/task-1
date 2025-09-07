from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/money/"

Path = "D:\\python\\autom-1\\task-1\\chromedriver-win64\\"

Service = Service(Path + "chromedriver.exe")
driver = webdriver.Chrome(service=Service)

driver.get(website)

cont = driver.find_elements(by="xpath", value='//a[@class="Wwrsb"]')

#/a[@class="Wwrsb"] , # //*[self::a or self::div][@class="Wwrsb"] [position() <= 400]