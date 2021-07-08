import requests
from bs4 import BeautifulSoup


URL = "https://www.snapdeal.com/product/redmi-rose-gold-6a-2gb/5764608145112238028"
URL = "https://www.snapdeal.com/product/samsung-samsung-galaxy-m11-64gb/5764608147400678360"
URL = "https://www.snapdeal.com/product/philips-philips-hp8302-hair-straightener/622317415870"
URL = "https://www.snapdeal.com/product/mamaearth-body-lotion-400-g-/661394749802"
URL = "https://www.snapdeal.com/product/ambrane-pp20-20000-mah-lipolymer/620725261183#bcrumbLabelId:12"


product_list = {'product_url': 'https://www.snapdeal.com/product/redmi-rose-gold-6a-2gb/5764608145112238028',
                'name': 'Redmi', 'target_price': 6000},\
       {'product_url': 'https://www.snapdeal.com/product/samsung-samsung-galaxy-m11-64gb/5764608147400678360' ,
        'name': 'Samsung', 'target_price': 11000},\
       {'product_url': 'https://www.snapdeal.com/product/philips-philips-hp8302-hair-straightener/622317415870',
        'name': 'Hair Straightener', 'target_price': 1250},\
       {'product_url': 'https://www.snapdeal.com/product/mamaearth-body-lotion-400-g-/661394749802',
        'name': 'Body Lotion', 'target_price': 400}, \
       {'product_url': 'https://www.snapdeal.com/product/ambrane-pp20-20000-mah-lipolymer/620725261183#bcrumbLabelId:12',
        'name': 'Power bank', 'target_price': 1000}


def product_price(URL):
    headers = {'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    # print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    cost = soup.find("span", {"class": "pdp-final-price"})
    if (cost == None):
        cost = soup.find("span", {"class": "payBlkBig"})

    return cost.getText()

result_file = open('result.txt','w')


try:
    for every_product in product_list:
        cost_returned = product_price(every_product.get('product_url'))
        print(cost_returned + " - " + every_product.get('name'))

        my_price = cost_returned[3:]
        my_price = my_price.replace(',', '')
        my_price = float(my_price)

        print(my_price)
        if my_price < every_product.get('target_price'):
            print("Available at your required price!\n")
            result_file.write(every_product.get('name') + ' : \t' + 'Available at target price!' +'\n\t\t\t' + 'Current price: ' + str(my_price) + '\n')
        else:
            print("Not yet in the range of target price.\n")
            #result_file.write(every_product.get('name') + ' : \t' + 'Not yet in the range of target price.' +'\n\t\t\t' + 'Current price: ' + str(my_price) + '\n')


finally:
    result_file.close()







