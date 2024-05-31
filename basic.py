import requests
from bs4 import BeautifulSoup
from pprint import pprint
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.safari.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def scrape_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we handle HTTP errors
    return BeautifulSoup(response.text, 'html.parser')

def get_pokemon_lis(soup):
    ul_element = soup.find('ul', class_='products')
    if ul_element:
        return ul_element.find_all('li', class_='product')
    else:
        print("No ul element found with class 'products'")
        return []

def parse_pokemon(li):
    name_element = li.find('h2', class_='woocommerce-loop-product__title')
    price_element = li.find('span', class_='price')
    
    if name_element and price_element:
        name = name_element.text
        price = price_element.text
        
        return {
            "title": name,
            "price": price,
        }
    else:
        if not name_element:
            print("Title element not found in li:", li)
        if not price_element:
            print("Price element not found in li:", li)
        return None

def main():
    pokemons = []
    pages = 2  # Number of pages to scrape

    for page in range(1, pages + 1):
        url = f"https://scrapeme.live/shop/page/{page}/"
        print(f"Scraping URL: {url}")
        soup = scrape_page(url)
        li_elements = get_pokemon_lis(soup)

        for li in li_elements:
            pokemon = parse_pokemon(li)
            if pokemon:
                pokemons.append(pokemon)

    pprint(pokemons)

if __name__ == "__main__":
    main()

    

""" driver = webdriver.Safari()

try:
    driver.get('https://scrapeme.live/shop/')

    driver.implicitly_wait(10)

    print(driver.page_source)
    
    element = driver.find_element(By.TAG_NAME, 'h1')
    href_value = element.get_attribute('href')
    print('Href attribute:', href_value)

    print('Element text:', element.text)


finally:
    driver.quit() """

""" print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
soup.prettify()
print (soup.prettify())

soup.head 
soup.body 
soup.title
print(soup.head)
print(soup.body)
print(soup.title)

paragraph = soup.body.div.p 
type(paragraph)
paragraph.name
paragraph.text
paragraph['class'] = 'newCLass' 
"""



