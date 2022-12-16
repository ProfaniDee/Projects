from selenium import webdriver

website = input('What webpage do you wish to go to?\n')
usr_login = input('What is your login?\n')
usr_pass = input('What is your password?\n')
browser = webdriver.Firefox()
browser.get('http://' + website +'/login')
login_elem = browser.find_element_by_id('input'or'username')
login_elem.send_keys(usr_login)
nextbuttonelem = browser.find_element_by_id('next')
nextbuttonelem.click()
passelem = browser.find_element_by_id('Passwd'or'password')
passelem.send_keys(usr_pass)
passelem.submit()
#website dependant, does not work on most sites