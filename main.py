from datetime import datetime
import json

from scrappers import GoogleScrapper, WebsiteScrapper

def run():
    search_key = input('Ingresa la palabra clave de búsqueda:\n>')
    print(f'Getting urls for {search_key}')
    urls = GoogleScrapper.get_urls_by_search_key(search_key)
    print(f'{len(urls)} Found')
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
    with open(file_name, 'w', encoding='UTF-8') as file:
        file.write(json.dumps(results))

    # TODO Agregar análisis de jsons. 

if __name__ == '__main__':
    run()