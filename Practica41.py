from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains


elchofer = webdriver.Chrome(r"D:\marioAdair\Universidad\SeptimoSemestre\testing\chromedriver_win32/chromedriver.exe")
elchofer.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

action = ActionChains(elchofer)

izq = elchofer.find_element(By.XPATH, '//*[@id="box1"]')
der = elchofer.find_element(By.XPATH, '//*[@id="box101"]')
action.drag_and_drop(izq, der).perform()

izq = elchofer.find_element(By.XPATH, '//*[@id="box2"]')
der = elchofer.find_element(By.XPATH, '//*[@id="box102"]')
action.drag_and_drop(izq, der).perform()

izq = elchofer.find_element(By.XPATH, '//*[@id="box3"]')
der = elchofer.find_element(By.XPATH, '//*[@id="box103"]')
action.drag_and_drop(izq, der).perform()

izq = elchofer.find_element(By.XPATH, '//*[@id="box4"]')
der = elchofer.find_element(By.XPATH, '//*[@id="box104"]')
action.drag_and_drop(izq, der).perform()

izq = elchofer.find_element(By.XPATH, '//*[@id="box5"]')
der = elchofer.find_element(By.XPATH, '//*[@id="box105"]')
action.drag_and_drop(izq, der).perform()

izq = elchofer.find_element(By.XPATH, '//*[@id="box6"]')
der = elchofer.find_element(By.XPATH, '//*[@id="box106"]')
action.drag_and_drop(izq, der).perform()

izq = elchofer.find_element(By.XPATH, '//*[@id="box7"]')
der = elchofer.find_element(By.XPATH, '//*[@id="box107"]')
action.drag_and_drop(izq, der).perform()