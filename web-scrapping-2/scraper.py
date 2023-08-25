from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

star_list = []

def scrape_more_data(url):
    url = START_URL
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    star_table = soup.find_all('table')
    table_rows = star_table[7].find_all('tr')
    for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
          
            for td_tag in td_tags:
                try: 
                    star_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    star_list.append("")

scrapped_data = []

headers = ["name", "distance", "mass", "radius"]
new_planet_df_1 = pd.DataFrame(scrapped_data,columns = headers)
new_planet_df_1.to_csv('draf_stars_data.csv',index=True, index_label="id")                    