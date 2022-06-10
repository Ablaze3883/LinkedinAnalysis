from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('C:\\Users\\chromedriver.exe')

# Logging into LinkedIn
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys('ag20223838@gmail.com')  # Enter Your Email Address

pword = driver.find_element_by_id("password")
pword.send_keys('@#Password@#')  # Enter Your Password

driver.find_element_by_xpath("//button[@type='submit']").click()


#URL of user profile here
profile_url = "https://www.linkedin.com/in/kunalshah1/"

driver.get(profile_url)


src = driver.page_source

#
soup = BeautifulSoup(src, 'lxml')

intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

name_loc = intro.find("h1")


name = name_loc.get_text().strip()


works_at_loc = intro.find("div", {'class': 'text-body-medium'})


works_at = works_at_loc.get_text().strip()

location_loc = intro.find_all("span", {'class': 'text-body-small'})


location = location_loc[1].get_text().strip()

print("Name -->", name,
      "\nWorks At -->", works_at,
      "\nLocation -->", location)