
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://hoopshype.com/salaries/players/")

elements = driver.find_elements(By.TAG_NAME, 'p')

for e in elements:
    print(e.text)