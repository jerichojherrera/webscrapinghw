
# coding: utf-8

# In[231]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd


# In[232]:



browser0 = Browser('chrome', headless=False)
url0 = 'https://mars.nasa.gov/news/'
browser0.visit(url0)
html0 = browser0.html
soup0 = bs(html0, 'html.parser')


# In[233]:



results0 = soup0.find_all('div')
for result0 in results0:
    try:
        #title
        title0 = result0.find('div', class_="bottom_gradient")   
    
        latest_title = title0.find('h3')
        
        news_title = latest_title.text
        
        #paragraph description
        
        para0 = result0.find('div', class_="article_teaser_body")
        
        news_p = para0.text
        
    
    except AttributeError:
        pass
    
    break


# In[234]:




print(news_title)
print(news_p)


# In[235]:




browser = Browser('chrome', headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[236]:



results = soup.find_all('div')
for result in results:
    try:
        title = result.find('h2', class_="brand_title")
        #title_text = title.a.text
    
        a = result.find('a', class_="button fancybox")
    
        #img = a.find('data-fancybox-href=')
        #print(title)
        print(a)
    
    except AttributeError:
        pass
    break


# In[237]:




#featured_image_url = 'https://www.jpl.nasa.gov/' + str()
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19685_ip.jpg'


# In[238]:




browser2 = Browser('chrome', headless=False)
url2 = 'https://twitter.com/marswxreport?lang=en'
browser2.visit(url2)
html2 = browser2.html
soup2 = bs(html2, 'html.parser')


# In[241]:



results2 = soup2.find_all('div')
for result2 in results2:
    try:
        title2 = result2.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
        
    
        
        latest_mars_weather_tweet = title2.text
        

    except AttributeError:
        pass
    break


# In[242]:



print(latest_mars_weather_tweet)


# In[243]:



mars_facts_url = 'https://space-facts.com/mars/'
table = pd.read_html(mars_facts_url)


# In[244]:




df = pd.DataFrame(table[0])
df.columns =['Description', 'Value']
df


# In[245]:




html_table = df.to_html()
#print(html_table)


# In[246]:


#df.to_html('table.html')


# In[247]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]

# Dependencies
from flask import Flask, render_template
import pymongo

# Create a Flask app
app = Flask(__name__)

# Connect to MongoDB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Use database and create it if it does not exist
db = client.marsDB

@app.route("/")
def index():
    #listings = db.listings.find_one()
    #print(latest_mars_weather_tweet)
    return render_template("index.html", listings=db)




if __name__ == "__main__":
    app.run(debug=True)
