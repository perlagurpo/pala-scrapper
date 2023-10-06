import requests
from bs4 import BeautifulSoup


class GoogleScrapper:
    
    @classmethod
    def get_urls_by_search_key(
        self,
        search_key
    ):
        start_item = 0
        urls = []
        while True:
            url = f'https://google.com/search?q={search_key}&start={start_item}'
            response = requests.get(url=url)
            try:
                soup = BeautifulSoup(response.content, 'html.parser')
                span = soup.find_all('span')
                span_urls = [url.text for url in span if 'www' in url.text]
                if span_urls == []:
                    break
                urls.extend(span_urls)
                start_item += 50
            except Exception as error:
                print(error)
                pass
        urls = list(set(urls))
        return urls
    
    