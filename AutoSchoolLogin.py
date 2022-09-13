from selenium import webdriver
import time

PATH = 'C:/Program Files (x86)/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=PATH, options=options)

driver.get("https://sislogin.edgenuity.com/")
driver.maximize_window()


def get_password():
    try:
        passwordFile = open("password.txt")
        return passwordFile.readline()
    except:
        return


def get_login():
    try:
        loginFile = open("username.txt")
        return loginFile.readline()
    except:
        return


def find_element_by_name(function_driver, name):
    try:
        return function_driver.find_element(by="name", value=name)
    except:
        return


# Get the login elements needed
loginField = find_element_by_name(driver, "tbLogin")
passwordField = find_element_by_name(driver, "tbPassword")
loginBtn = find_element_by_name(driver, "btLogin")

# Fill in username & password then login
loginField.send_keys(get_login())
time.sleep(0.05)
passwordField.send_keys(get_password())
time.sleep(0.05)
loginBtn.click()

# Open the school page and click the continue button
driver.get("https://e2020.geniussis.com/FESSOLMS.aspx?eid=4211390")
continueButton = find_element_by_name(driver, "continue")
continueButton.click()
