from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd
# from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
        executable_path = {'executable_path': "./chromedriver"}
        return Browser("chrome", **executable_path, headless=True)

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
    news_title = results.a.text

    #Get article description
    results2 = soup.find('div', class_= "rollover_description_inner")

    #Get text from article description/define variable
    news_preview = results2.text.strip()

   
    #Visit the url for the image
    getimage_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(getimage_url)

    # Retrieve page with the requests module
    # response_image = requests.get(getimage_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    # soup_image = bs(response_image.text, 'html.parser')

    #Get image from soup object
    # image = soup_image.find_all('div', class_ ='floating_text_area')

    #Use splinter to select button to see full image
    # browser.links.find_by_partial_text('FULL').click()

    #URL for feature image
    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg"

    #Use Pandas to scrape info in to datatable
    #Get get desired info by index
    #Rename df columns
    #Convert df to HTMLS
    #Clean HTML table of '\n'
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    df = tables[0]
    df.columns = ['Description', '']
    html_table = df.to_html()
    html_table_clean = html_table.replace('\n', '')

    #URL for Hemisphere information
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(browser.html, 'html.parser')

    #Get info from soup object
    divs = soup.find_all('div', class_ ='item')
    print(divs)

    
    #Base URL for image URLS
    base_url = 'https://astrogeology.usgs.gov'

    #Get info for hemispheres title and urls
    hemisphere_dict = []
    for div in divs:
                a_tag = div.find("a")
                img_url = base_url + a_tag.attrs['href']
                browser.visit(img_url)
                soup = bs(browser.html, "html.parser")
                img_url = soup \
                    .find("div", class_="wide-image-wrapper") \
                    .find('li') \
                    .find("a").attrs['href']
                title = soup \
                    .find('div', class_='content') \
                    .find('h2').text
                temp_dict = {'title' : title, 'img_url':img_url}
                hemisphere_dict.append(temp_dict)


    mars_data = {
       "news_title": news_title,
       "news_preview": news_preview,
       "featured_image_url": featured_image_url,
       "html_table_clean": html_table_clean,
       "hemisphere_dict": hemisphere_dict
    }
  
    browser.quit()

    #Return results
    return mars_data






