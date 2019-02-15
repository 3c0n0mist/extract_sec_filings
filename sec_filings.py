from selenium import webdriver
import pyperclip
import sys

browser = webdriver.Safari()
browser.get('https://www.sec.gov/edgar/searchedgar/companysearch.html')
searchElem = browser.find_element_by_id('cik')

# search for compay filings on sec
if len(sys.argv)>1:
    cont = ''.join(sys.argv[1:])

else:
    cont = pyperclip.paste

searchElem.send_keys(cont)

searchElem.send_keys(u'\ue007')

# # search for 10K
# searchElem.send_keys( u'\ue004')
# searchElem.send_keys('10-K')
# searchElem.send_keys(u'\ue007')
#
# # click on the latest 10K
# searchBar = browser.find_element_by_id('interactiveDataBtn')
# searchBar.click()



