# Importēju visas nepieciešamās bibliotēkas

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

"""
Inicializēju jaunu servisu "service", kā arī "webdriver.ChromeOptions",
lai varu strādāt ar interneta pārlūku "Google Chrome"
"""
service = Service()
option = webdriver.ChromeOptions
driver = webdriver.chrome(service=service, options=option)

# Norādu nepieciešamās vietnes url 

url = "https://www.rtu.lv/lv/sports"
driver.get(url)

# Atrodu elementu ar attiecīgu KLASES VĀRDU dodu pavēli uzspiest, lai apstiprinātu sīkdatnes, apstādinu programmas tālāku darbību uz 1 sekundi

accept_cookies = driver.find_element(By.CLASS_NAME,"uce-accept")
accept_cookies.click()
time.sleep(1)

# Atrodu elementu ar attiecīgu ID un dodu pavēli uzspiest, lai naviģētu uz vietnes izvēlnes sadaļu

menu = driver.find_element(By.ID, "mobile_menu_button")
menu.click()

# Atrodu elementu ar attiecīgu LINK TEXT, un dodu pavēli uzspiest, lai atrastu sadaļu "ieiet" un kas mani pārmet uz citu lapu

login = driver.find_element(By.LINK_TEXT, "🏃  Ieiet")
login.click()

"""
Atrodu 2 elementus ar attiecīgiem ID un dodu pavēli ievadīt nepieciešamos datus, un atrodu elementu ar attiecīgu NAME, lai apstiprinātu ievadītos datus.
Sakarā ar to, ka tieku atkal pārmests uz citu lapu, apstādinu programmas tālāku darbību uz 1 sekundi
"""

user = driver.find_element(By.ID,"IDToken1")
user.send_keys("Lietotājvārds")

password = driver.find_element(By.ID, "IDToken2")
password.send_keys("Parole")

login_accept = driver.find_element(By.NAME,"Login.Submit")
login_accept.click()
time.sleep(1)

# Vēlreiz atrodu elementu ar attiecīgu ID un dodu pavēli uzspiest, lai naviģētu uz vietnes izvēlnes sadaļu

menu = driver.find_element(By.ID, "mobile_menu_button")
menu.click()

# Atrodu elementu ar attiecīgu LINK TEXT un dodu pavēli uzspiest, kas mani pārmet uz nodarbību lapu. Apstādinu programmas tālāku darbību uz 1 sekundi

activities = driver.find_element(By.LINK_TEXT, "⚽ Pieteikties nodarbībām")
activities.click()
time.sleep(1)

# Atrodu elementu ar attiecīgu KLASES VĀRDU un dodu pavēli uzspiest, lai pārmainītu grafika izklājumu uz ikdienas

day = driver.find_element(By.CLASS_NAME, "fc-agendaDay-button")
day.click()

"""
Sakarā ar to, ka notikumi kalendārā regulāri mainās un ir statiski, katram notikumam 
elementu noskaukums ir vienāds, tāpēc atrodu visus elementus ar attiecīgo KLASES VĀRDU un dodu pavēli uzspiest uz tā, kurš ir vajadzīgs man. 
"""

gym = driver.find_elements(By.CLASS_NAME, "fc-title")
gym[8].click()

# Atrodu elementu ar attiecīgu KLASES VĀRDU un dodu pavēli uzspiest, lai veidotu pieteikumu uz trenežieru zāli, kā arī elementu ar attiecīgu XPATH, lai apstiprinātu pieteikumu

pieteikt=driver.find_element(By.CLASS_NAME, "unibit_modal_show")
pieteikt.click()

confirm=driver.find_element(By.XPATH, "//*[@id='modal_apply']/div/div/div/div/form/div[2]/div[1]/input")
confirm.click()

# Atrodu elementu ar attiecīgu XPATH un dodu pavēli uzspiest, lai apmaksātu manu pieteikumu un pabeigtu uzdevumu

pay=driver.find_element(By.XPATH, "/html/body/div[2]/div/form[1]/table[2]/tbody/tr/td[1]/button")
pay.click()

# Izveidoju ievades logu beigās, lai programma iet līdz tam brīdim, kad uzspiež jebkuru pogu uz klavietūras un programma apstājas

input()

