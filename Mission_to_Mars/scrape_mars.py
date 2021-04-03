from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
        executable_path = {'executable_path': "./chromedriver"}
        return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
        
    #Visit the url for news article information
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')

    #Get article title from soup object
    results = soup.find('div', class_='content_title')

    #Get text for article name from results/define variable
    news_title = results.get_text()

    #Get article description
    results2 = soup.find('div', class_= "rollover_description_inner")

    #Get text from article description/define variable
    news_p = results2.text.strip()

   
    #Visit the url for the image
    getimage_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(getimage_url)

    # Retrieve page with the requests module
    response_image = requests.get(getimage_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_image = bs(response_image.text, 'html.parser')

    #Get image from soup object
    image = soup_image.find_all('div', class_ ='floating_text_area')

    #Use splinter to select button to see full image
    browser.links.find_by_partial_text('FULL').click()

    #URL for feature image
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg'

    #Use Pandas to scrape info in to datatable
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    df = tables[0]
    df.columns = ['Description', '']
    html_table = df.to_html()
    html_table_clean = html_table.replace('\n', '')


    #Informational URLSs
    hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
]


    mars_data = {
        "news_title": news_title,
        "news_preview": news_p,
        "image": featured_image_url,
        # "image2": image,
        "info_table": html_table_clean,
        "hemishphere_image_urls": hemisphere_image_urls
    }

    browser.quit()

    return mars_data






