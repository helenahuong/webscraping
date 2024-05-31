from bs4 import BeautifulSoup
import requests
import time
import random

url = 'https://www.amazon.com/s?k=imac+desktop+computer&crid=2N1HS3WKJVCMQ&sprefix=imac%2Caps%2C458&ref=nb_sb_ss_ts-doa-p_2_4'

proxies = {
    'http': 'http://104.207.51.91:3128',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'csm-hit=tb:s-KMH0MM8YFZTFKHM2CDD4|1717167489451&t:1717167490394&adb:adblk_no; session-token="1do4qHH15ApvcO66lU4Mf/ou3VtwDYf0FVCYUaXFnhWGKDA9a/XFtXZ1Eu81gpgnvfbJKhD2js2u7dC9Hjq/BDgd8zbFek959p7Y9yGDCtG2HmAFEg+1Fiy3mAGMsyWo32ED9IUGrl2ltuQ6D2qw/FI6gSi1lESvp7rysMWKRVJjC34y8h9iQzeBA8zlDlDq4vSHV0F3OXnYe+O+yxytRWnjCXcD3mmx5ha1V+6GizCRNSBkRL/MYLnaC/X16tuBcB/cdFOSEY4aBoulOFQDoJCj9nxhiP8loWBgOGKKJil54tS1tL685yIenf6LeHQiFd3TrGXOUBpt6fe2MJ0ik+C0zIvruotOG6gyKuykGqI9UA3Wc4cmsQVBeONB7T/T0td2Y5rSxjQYOuzKW1qAB8MKTIDlepTnWAw1YGr3D22xXRp2wcJ19w=="; session-id=130-6218674-6468118; session-id-time=2082787201l; ubid-main=131-7548663-3769404; skin=noskin; regStatus=pre-register; s_campaign=em%7C2477a117-cd4d-42fe-8fb2-c10b2d1944fb; s_eVar60=2477a117-cd4d-42fe-8fb2-c10b2d1944fb; s_sq=awsamazonallprod1%252Cawsamazonallprodcopy1%252Cawsamazonallprodcopy2%3D%2526pid%253Daws.amazon.com%25252Fevents%25252Fsummits%25252Fsingapore%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fpages.awscloud.com%25252Faws-summit-singapore-on-demand-registration.html%25253Ftrk%25253D2477a117-cd4d-42fe-8%2526ot%253DA; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19859%7CMCMID%7C67556960350995546540997126457763004231%7CMCAAMLH-1716370381%7C3%7CMCAAMB-1716370381%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1715772781s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19866%7CvVersion%7C4.4.0; AMCVS_7742037254C95E840A4C98A6%40AdobeOrg=1; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1715765581507-555616.48_0; s_cc=true; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1714982063924-36809; aws_lang=en; lc-main=en_US; pay-session-id=782943193edfd14d5e41730da23b5378; at-main=Atza|IwEBII0AiZ8fC0hcCVyeN-hV5wYFuToSvN7x5Yi7RVY676PKWSB4e_l7rOOSfvaZ85Wq0IXX06nkfbWcZcUqKdaCgMnjK2J7TTYocyOeBFtn4Fh10Kn3qXjw7CdzNY1ErinHa1J7ncCUugQk67iCjovE9404ztlh2BbWLBJHb6dU6cHRQvzvZalUW4QsbnCz49bIeWrM8qzSfmcp5WKMffu3sYfWU1O5HjbijiFxWsr4JkYfi8Hv_ZGYz8k48tX7sIsPUA-Nfa2Dzowfaz_A8EYT5asKlObX5HmAHOjL3IAe2vAg4v0jrv9AOgkRkKLiOioDM-_NFfBtxxrHcC2hy0eCxULN; sess-at-main=VeuOMZMaxKQmuiCh6DCodiZpsHFWoXRdn7I03g+PnOU=; i18n-prefs=USD; x-main="J8B7Pe7PMpEOIyRq?KLnLMu9XKuM7xxYzmmCNEIAGkW6Lvz4F8pffLLd4nO2JymM"; sst-main=Sst1|PQH2_AaLi8Ndr0gDnJBQTCGHCb8ShoDRWIsHB3EzPevWjcCT0QzeKyvPr3MZ3KcmjZePHqzYFpU-2Eb9latJzDPRd_9hq11yWczXVymZ1IJ28lmLkna8LjhDj504khyWrvVkGae5N9McsgzaHTtqmJJ5VRcf8Od5LIxddeKaprIG4SP1REP75Pg79HMPqdqrFjl239s97WHOUlyc-f3wxo__RLDzuQtMDVw9VUNIj_X8SnZd5JLFURLZQ3S1UE_afeaf3aCQB-Lw79adCAVZonJId4MDvaIPSyVQW8JPVo-CBME',
    'Host': 'www.amazon.com',
    'Priority': 'u=0, i',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
}

def make_request(url, proxies, headers):
    for _ in range(5):  # Retry up to 5 times
        response = requests.get(url, proxies=proxies, headers=headers)
        if response.status_code == 200:
            return response
        elif response.status_code == 503:
            print("Received 503, retrying...")
            time.sleep(random.uniform(1, 3))  # Sleep between 1 and 3 seconds
        else:
            print(f"Unexpected status code: {response.status_code}")
            break
    return None

response = requests.get(url, proxies=proxies, headers=headers)
if response:
    print(response.status_code)
    print(response.text)
else:
    print("Failed to retrieve the page after several attempts.")

def parse_products(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    
    for item in soup.select('.s-main-slot .s-result-item'):
        title_element = item.select_one('h2 .a-text-normal')
        price_element = item.select_one('.a-price-whole')
        
        if title_element and price_element:
            title = title_element.text.strip()
            price = price_element.text.strip()
            products.append({
                'title': title,
                'price': price
            })
    
    return products

def main():
    response = make_request(url, proxies, headers)
    if response:
        print(response.status_code)
        products = parse_products(response.text)
        for product in products:
            print(f"Title: {product['title']}, Price: {product['price']}")
    else:
        print("Failed to retrieve the page after several attempts.")

if __name__ == "__main__":
    main()
