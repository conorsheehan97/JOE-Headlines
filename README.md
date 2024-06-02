# JOE.ie-Headlines
## Overview
This project scrapes the JOE.ie website for the top 10 headlines in Sports, Entertainment, and Politics categories. It saves the headlines, links, and categories to a local SQL database on your desktop with today's date appended.

## Purpose
The goal is to gather relevant news headlines from JOE.ie and store them locally for easy access and reference.

## Methodology
### Web Scraping:
 - Sends a GET request to the JOE.ie homepage.
 - Parses the HTML response using BeautifulSoup to extract headlines, links, and categories for Sports, Entertainment, and Politics.
### Data Storage:
 - Utilizes SQLite3 to create and manage a local database.
 - Stores scraped data including headline text, article link, category, and date of scraping.
## Libraries Used
 - Pandas
 - SQLite3
 - BeautifulSoup (bs4)
 - Datetime
 - Requests
## Usage
 - Run the scraping script periodically to update the local database with the latest headlines from JOE.ie.
 - Access the SQLite database to view stored headlines and their details.
## Notes
 - Ensure compliance with JOE.ie's robots.txt guidelines when scraping.
 - Customize the scraping script or database schema as needed for additional functionality or data storage requirements.
