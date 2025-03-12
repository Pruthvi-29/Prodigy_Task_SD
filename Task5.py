import requests
from bs4 import BeautifulSoup
import pandas as pd


baseurl = "https://www.thewhiskyexchange.com"


def scrape_products():
    product_links = []
    data = []
    
    
    for page in range(1, 6):
        url = f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={page}&psize=24&sort=pasc'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
     
        product_list = soup.find_all("li", {"class": "product-grid__item"})
        
        for product in product_list:
            link = product.find("a", {"class": "product-card"}).get('href')
            product_links.append(baseurl + link)

   
    for link in product_links:
        product_response = requests.get(link)
        product_soup = BeautifulSoup(product_response.text, 'html.parser')
        

        try:
            name = product_soup.find("h1", {"class": "product-main__name"}).text.strip()
        except:
            name = None
        
        try:
            price = product_soup.find("p", {"class": "product-action__price"}).text.strip()
        except:
            price = None
        
        try:
            rating = product_soup.find("div", {"class": "review-overview"}).text.strip()
        except:
            rating = None
        
       
        product_data = {
            "Name": name,
            "Price": price,
            "Rating": rating
        }
        data.append(product_data)

   
    df = pd.DataFrame(data)
    df.to_csv('whisky_products.csv', index=False, encoding='utf-8')
    print("Data has been successfully scraped and saved to 'whisky_products.csv'.")

if __name__ == "__main__":
    scrape_products()