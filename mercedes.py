import requests
from bs4 import BeautifulSoup
from Random_headers import random_headers

def mers_parse():
    # ua = FakeUserAgent().random
    towns_list= ['moscow', 'novosibirsk', 'rostov-na-donu', 'kazan', 'ekaterinburg']
    x = 1
    mers_dict = {}
    for town in towns_list:
        average_price = 0
        for i in range(x):
            req = requests.get(f'https://{town}.drom.ru/mercedes-benz/all/page{i}/?minyear=2012',
                               headers=random_headers()).text
            soup = BeautifulSoup(req, 'lxml')
            cars_parse = soup.find('div', class_="css-1nvf6xk eaczv700").find_all('a')

            cars_urls = []
            for item in cars_parse:
                final_url = item['href']
                cars_urls.append(final_url)

            total_price = 0
            count = 1
            for item in cars_urls:
                try:
                    req = requests.get(item, headers=random_headers())
                    soup = BeautifulSoup(req.text, 'lxml')
                    # date = soup.find('div', class_="css-pxeubi evnwjo70").text
                    # date = date.split()[-1]
                    price = soup.find('div', class_="css-eazmxc e162wx9x0").text
                    price = int(''.join(c for c in price if c.isalnum()))
                    total_price += price
                    count += 1
                except:
                    continue
            av_by_page = int(total_price/count)
            average_price += av_by_page
        final_average = int(average_price/x)
        mers_dict[town] = final_average
    return mers_dict
