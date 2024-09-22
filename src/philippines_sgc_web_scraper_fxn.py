
# libraries for webscrapping
from bs4 import BeautifulSoup
import requests

# dataframes package
import pandas as pd

# function to web scrape 
# takes arguments: page_url: website url address
 
def ph_sgc_web_scraper(page_url):
    # url page request
    page = requests.get(page_url)

    # get text from page using parser html
    soup = BeautifulSoup(page.text, 'html.parser')
 
    # check if there's are more than one table
    # if table > 1 ask to check which table to scrape

    table = soup.find('table')


    # get headers from  the tables
    table_titles = table.find_all('th') # results have <th>
    # grabbing only the text
    table_headers = [title.text for title in table_titles]

    # print table headers
    print("table headers", table_headers, sep= ":")

    # creating an empty dataframe with table headers
    # philippines municipality income classes
    ph_mun_inc_class = pd.DataFrame(columns = table_headers)

    # getting the table data
    column_data = table.find_all('tr') # table rows

    # iterate over each row starting from index 1 coz of empty list at index 0
    for row in column_data[1:]: # start from position 1 coz of the empty list at index 0
        #print(row.find_all('td'))
        row_data = row.find_all('td')
        # using comprehensions to clean up and extra clean row data
        cln_row_data = [data.text for data in row_data]
    
        # append each row to dataframe ph_mun_inc_class
        ## keep check on the curr index of the dataframe
        length = len(ph_mun_inc_class)
        ph_mun_inc_class.loc[length] = cln_row_data

        # return the dataframe
    return ph_mun_inc_class