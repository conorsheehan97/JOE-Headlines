#Here we import our modules for creating https requests, web scraping, dataframe work, creating our sql db
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from datetime import datetime

#This ensures this code only runs if being called directly
if __name__ == '__main__':
    #Here we define our function which takes in links from a beautiful soup object
    #as well as the link type
    def create_title_link_list(links, link_category):
        #declaring 3 lists for the headline, headline link, and headline category
        headlines = []
        headline_link = []
        headline_category = []
        #enumerating our links to get both the index, and link itself
        for idx, item in enumerate(links):
            #setting titles variable to the actual text of the headline
            titles = links[idx].getText()
            #setting url variable to the href attribute of the link element
            urls = links[idx].get('href', None)
            #appending our variables to the lists, minus any junk (\n)
            headlines.append(titles.strip('\n'))
            headline_link.append(urls)
            headline_category.append(link_category)
        #Creating a dataframe to return
        headline_dataframe = pd.DataFrame(
            {'Headline': headlines, 'Headline URL': headline_link, 'Category': link_category})
        return headline_dataframe

    #Creating our lists to iterate through on the JOE website
    #We use 2 lists here as the URL text is slightly off what we want the category saved as
    JOE_Categories = ['Sport', 'News', 'Movies & TV', 'Lifestyle', 'Politics', 'Quiz', 'Fitness & Health', 'Tech']
    JOE_Categories_URL = ['sport', 'news', 'movies-tv', 'life-style', 'politics', 'quiz', 'fitness-health', 'tech']

    #Instantiating a Dataframe
    articles = pd.DataFrame()

    #Iterating through the list pair
    for category_url, category in zip(JOE_Categories_URL, JOE_Categories):
        #URL construction by adding strings
        URL = 'https://www.joe.ie/category/' + category_url
        #Sending a GET request to the constructed url and saving the response to the requests variable
        res = requests.get(URL)
        #Using the beautiful soup parser to parse the html response
        soup = BeautifulSoup(res.text, 'html.parser')
        #Selecting only the first 10 elements wit the class underlineTitles
        links = soup.select('.underlineTitles')[:10]
        #adding the headlines to our dataframe. This is done per category in JOE_Categories
        articles = pd.concat([articles, create_title_link_list(links, category)], ignore_index=True)

    # Get current date
    current_date = datetime.now()

    # Format date as "dd mm yyyy"
    formatted_date = current_date.strftime("%d-%m-%Y")

    articles['Date'] = formatted_date

    # Connect to the SQLite database
    conn = sqlite3.connect('JOE_Headlines.db')

    # Append DataFrame to an existing SQL table
    articles.to_sql('headlines', conn, if_exists='append', index=False)

