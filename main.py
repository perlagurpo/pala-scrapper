from datetime import datetime
import json
import re

from scrappers import GoogleScrapper, WebsiteScrapper

def run():
    search_key = input('Ingresa la palabra clave de búsqueda:\n>')
    urls = get_urls(search_key)
    results = get_results(urls, search_key)
    data = parse_results(results, search_key)
    
    return data

def get_urls(search_key):
    print(f'Getting urls for {search_key}')
    urls = GoogleScrapper.get_urls_by_search_key(search_key)
    print(f'{len(urls)} Found')
    return urls

def get_results(urls, search_key):
    results = []
    for url in urls:
        try:
            print(f'Scraping {url}')
            html = WebsiteScrapper.get_html_from_url(url)
            footer_data = WebsiteScrapper.get_footer_data_from_html(html)
            footer_data['url'] = url
            results.append(footer_data)
        except Exception as error:
            print(error)
    print(f'{len(results)} Websites with contact data')
    file_name = f'files/results/{search_key}__{datetime.now()}.json'
    if results:
        with open(file_name, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(results))
    return results


def parse_results(results, search_key):
    data = []
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    year_pattern = r'\b20\d{2}\b'
    phone_pattern = r'\b(?:\+\d{1,3}\s?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
    for result in results:
        site = {
            'url': result['url'],
            'years': [],
            'emails': [],
            'phones':[]
        }
        all_text = result['copyright'] + result['footer']
        for text in all_text:
            year = re.findall(year_pattern, text)
            if year:
                site['years'].append(year[0])
            email = re.findall(email_pattern, text)
            if email:
                site['emails'].append(email[0])
            phone = re.findall(phone_pattern, text)
            if phone:
                site['phones'].append(phone[0])
        site['years'] = list(set(site['years'])) if site['years'] else ''
        site['emails'] = list(set(site['emails'])) if site['emails'] else ''
        site['phones'] = list(set(site['phones'])) if site['phones'] else ''
        data.append(site)
    file_name = f'files/parsed/{search_key}__{datetime.now()}.json'
    if data:
        with open(file_name, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(data))
    return data
if __name__ == '__main__':
    run()