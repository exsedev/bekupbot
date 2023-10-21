import pandas as pd
from selenium import webdriver
import time

def fill_form():
    data = pd.read_csv('emaildata.csv')
    recycle = data.shape[0]
    for i in range(recycle):
        print(i)
        driver = webdriver.Chrome()
        driver.get('https://heybeluga.com/')
        time.sleep(3)

        email = data.iloc[i]['email']
        inputEmail = driver.find_element("xpath",'//*[@id="newsletter-signup"]/input')
        for j in email:
            inputEmail.send_keys(j)
            time.sleep(0.05)
        time.sleep(1)

        submit = driver.find_element("xpath",'//*[@id="newsletter-signup"]/button')
        submit.click()
        time.sleep(5)

        # backForm = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        # backForm.click()
        # time.sleep(1)

fill_form()
time.sleep(220)