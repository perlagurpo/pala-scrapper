import time
import requests
from bs4 import BeautifulSoup


class Scrapper:
    
    @classmethod
    def get_urls_by_search_key_from_google(
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
                print(len(span_urls))
                if span_urls == []:
                    break
                urls.extend(span_urls)
                start_item += 50
            except Exception as error:
                print(error)
                pass
                
        urls = set(urls)
        print(urls)
        return urls
    
    @classmethod
    def get_html_data_from_url(self, url):

        response = requests.get(
            url=f'http://{url}',
            
        )
        print(response.status_code)
        with open(f'./files/GET__{url.replace("/","")}.txt', 'w') as file:
            file.write(response.text)
        return response.text
    
    @classmethod
    def get_data_from_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.find_all('div')
        footer = soup.find_all('footer')
        copy_rights = [div.text for div in divs if '©' in div.text]
        for i in range(len(copy_rights)):
            copy_rights[i] = copy_rights[i].replace('\n', '')
        data = {
            'copyright': copy_rights
        }    
        return data

