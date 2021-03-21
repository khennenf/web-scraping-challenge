# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# import time
# import requests
# # import pandas as pd
# from webdriver_manager.chrome import ChromeDriverManager

# def init_browser():
#         executable_path = {'executable_path': ChromeDriverManager().install()}
#         return Browser("chrome", **executable_path, headless=False)

# def scrape_info():
#     browser = init_browser()
    
#     #Visit the url
#     url = 'https://mars.nasa.gov/news/'
#     browser.visit(url)

#     #Retrieve page with the requests module
#     response = requests.get(url)

#     #Create BeautifulSoup object; parse with 'html.parser'
#     soup = bs(response.text, 'html.parser')

#     #Get results
#     results = soup.find('div', class_='content_title')

#     #Save news_title
#     news_title = results.a.text

#     #Get next results
#     results2 = results2 = soup.find('div', class_= "rollover_description_inner")

#     #Save news_preview
#     news_p = results2.text.strip()

#     #Break between sites
#     time.sleep(1)

#     #Visit url for image
#     url_image = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
#     browser.visit(url_image)

#     #Retrieve page with the requests module
#     response_image = requests.get(url_image)

#     #Create BeautifulSoup object; parse with 'html.parser'
#     soup_image = bs(response_image.text, 'html.parser')

#     #Navigate to next page
#     browser.links.find_by_partial_text('FULL').click()

#     #URL for image
#     featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg'

#     #URL for space-facts
#     facts_url = 'https://space-facts.com/mars/'

#     #Get data from space-facts
#     tables = pd.read_html(facts_url)
    
#     #Get image urls
#     hemisphere_image_urls = [
#     {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
#     {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
#     {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
#     {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
#     ]








  
   



    





