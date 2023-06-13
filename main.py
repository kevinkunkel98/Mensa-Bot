import requests
from bs4 import BeautifulSoup
import re
from telegram import Bot


def scrape_mensa_menu():
    url = 'https://www.studentenwerk-leipzig.de/mensen-cafeterien/speiseplan'
    response = requests.get(url)

    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the menu data using the section class "meals"
    menu_section = soup.find('section', class_='meals')
    # Extract the menu items within the section
    menu_items = menu_section.find_all('h4', class_='meals__name')

    menu_data = [re.search(r'<h4.*?>(.*?)</h4>', str(item)).group(1) for item in menu_items]
    # Process the menu items as per your requirements

    for menu in menu_data:
        print(menu)

if __name__ == '__main__':
    scrape_mensa_menu()
