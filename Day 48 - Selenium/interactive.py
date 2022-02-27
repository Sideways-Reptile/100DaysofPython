from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Users\\iAntagon1st\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
#
# print(article_count.text)
# locates links on pages and uses .click to click on them
# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# found the searhc by name (inspect) and used send_keys to type in the search bar
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# go = driver.find_element_by_name("go")
# go.click()


############## CHALLENGE TWO ###################

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
first_name.send_keys("Sergio")
last_name.send_keys("Taylor")
email.send_keys("sidewaays666@gmail.com")

sign_up = driver.find_element_by_class_name("btn")
sign_up.click()

