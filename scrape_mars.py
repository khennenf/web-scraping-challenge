from splinter import Browser
# from bs4 import BeautifulSoup as bs
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import pandas as pd

# def init_browser():
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)


# def scrap_info():
#     browser = init_browser()
#     url = 'https://mars.nasa.gov/news/'
#     browser.visit(url)

#     response = requests.get(url)
#     soup = bs(url, 'html.parser')

#     results = soup.find('div', class_='content_title')
#     news_title = results.a.text

#     results2 = soup.find('div', class_= "rollover_description_inner")
#     news_p = results2.text.strip()

#     browser.quit()



    





