# JOE-Headlines
This project simply scrapes the JOE.ie website for the top 10 headlines, in Sports, Entertainment &amp; Politics, and saves the headlines, links and categories to a SQL database on my local desktop. Nice to get some news from home and all that good stuff. 

Here we simply just send our GET request to the JOE.ie website homepage, parse our response using BeautifulSoup, and pick out our 10 headlines per category. These are then appended to a database stored locally on my own desktop, with todays date appended. Could simply just click on the website I suppose, but nice to be able to scrape relevant information and store it locally too. Having checked the robots.txt all is OK with scraping headlines too. 

Libraries used: Pandas, SQLite3, BeautifulSoup, Datetime, Requests
